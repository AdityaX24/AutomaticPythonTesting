import { useRef, useState } from "react";
import {
  FaCloudUploadAlt,
  FaSpinner,
  FaTimes,
  FaCheckCircle,
  FaExclamationTriangle,
} from "react-icons/fa";
import { uploadScript } from "../api";
import "./ScriptUpload.css";

interface UploadResult {
  filename: string;
  saved_as?: string;
  status: "success" | "error" | "rejected";
  message: string;
}

export const ScriptUpload = () => {
  const fileInput = useRef<HTMLInputElement>(null);
  const [dragActive, setDragActive] = useState(false);
  const [uploadResults, setUploadResults] = useState<UploadResult[]>([]);
  const [isUploading, setIsUploading] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(e.type === "dragenter" || e.type === "dragover");
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files?.length) {
      const newFiles = Array.from(e.dataTransfer.files);
      setSelectedFiles((prev) => [
        ...prev,
        ...newFiles.filter((f) => !prev.some((pf) => pf.name === f.name)),
      ]);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.length) {
      const newFiles = Array.from(e.target.files);
      setSelectedFiles((prev) => [
        ...prev,
        ...newFiles.filter((f) => !prev.some((pf) => pf.name === f.name)),
      ]);
    }
  };

  const removeFile = (index: number) => {
    setSelectedFiles((prev) => prev.filter((_, i) => i !== index));
  };

  const handleUpload = async () => {
    if (!selectedFiles.length) return;

    setIsUploading(true);
    setUploadResults([]);

    try {
      const formData = new FormData();
      selectedFiles.forEach((file) => {
        formData.append("files", file);
      });

      const response = await uploadScript(formData);
      setUploadResults(response.details);

      if (response.details.some((r: UploadResult) => r.status === "success")) {
        setSelectedFiles([]);
        if (fileInput.current) fileInput.current.value = "";
      }
    } catch (error) {
      setUploadResults([
        {
          filename: "All files",
          status: "error",
          message: "Upload failed. Please try again.",
        },
      ]);
    } finally {
      setIsUploading(false);
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case "success":
        return <FaCheckCircle className="success" />;
      case "error":
        return <FaExclamationTriangle className="error" />;
      case "rejected":
        return <FaExclamationTriangle className="warning" />;
      default:
        return null;
    }
  };

  return (
    <div className="script-upload-container">
      <div
        className={`drag-drop-zone ${dragActive ? "active" : ""}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <FaCloudUploadAlt className="upload-icon" />
        <p>Drag and drop Python scripts here</p>
        <span>OR </span>
        <br />
        <label className="browse-button">
          Browse Files
          <input
            type="file"
            ref={fileInput}
            onChange={handleFileSelect}
            hidden
            multiple
            accept=".py"
          />
        </label>
        <small className="file-requirements">
          Only .py files allowed • Max 10 files at once
        </small>
      </div>

      {selectedFiles.length > 0 && (
        <div className="files-preview">
          {selectedFiles.map((file, index) => (
            <div key={index} className="file-preview">
              <div className="file-info">
                <span className="file-name">{file.name}</span>
                <span className="file-size">
                  {(file.size / 1024).toFixed(2)} KB
                </span>
              </div>
              <button
                className="remove-file"
                onClick={() => removeFile(index)}
                title="Remove file"
                disabled={isUploading}
              >
                <FaTimes />
              </button>
            </div>
          ))}
        </div>
      )}

      <button
        onClick={handleUpload}
        className="upload-button"
        disabled={selectedFiles.length === 0 || isUploading}
      >
        {isUploading ? (
          <>
            <FaSpinner className="spin" />
            Uploading {selectedFiles.length} File
            {selectedFiles.length !== 1 ? "s" : ""}...
          </>
        ) : (
          `Upload ${selectedFiles.length} File${
            selectedFiles.length !== 1 ? "s" : ""
          }`
        )}
      </button>

      {uploadResults.length > 0 && (
        <div className="upload-results">
          {uploadResults.map((result, index) => (
            <div key={index} className={`result-message ${result.status}`}>
              {getStatusIcon(result.status)}
              <div className="result-details">
                <strong>{result.filename}</strong>
                <span>{result.message}</span>
                {result.saved_as && result.saved_as !== result.filename && (
                  <small>Saved as: {result.saved_as}</small>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
