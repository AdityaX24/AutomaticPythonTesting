import { useRef, useState } from "react";
import { FaCloudUploadAlt, FaSpinner } from "react-icons/fa";
import { uploadScript } from "../api";
import "./ScriptUpload.css";

export const ScriptUpload = () => {
  const fileInput = useRef<HTMLInputElement>(null);
  const [dragActive, setDragActive] = useState(false);
  const [uploadStatus, setUploadStatus] = useState<
    "idle" | "success" | "error"
  >("idle");
  const [uploadMessage, setUploadMessage] = useState("");
  const [isUploading, setIsUploading] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setSelectedFile(e.dataTransfer.files[0]);
      if (fileInput.current) {
        fileInput.current.files = e.dataTransfer.files;
      }
    }
  };

  const handleUpload = async () => {
    if (!fileInput.current?.files?.[0]) return;

    setIsUploading(true);
    setUploadStatus("idle");
    setUploadMessage("");

    try {
      const formData = new FormData();
      formData.append("file", fileInput.current.files[0]);
      formData.append("type", "script");

      await uploadScript(formData);
      setUploadStatus("success");
      setUploadMessage("File uploaded successfully!");
      setSelectedFile(null);
      if (fileInput.current) fileInput.current.value = "";
      setTimeout(() => setUploadStatus("idle"), 3000);
    } catch (error) {
      setUploadStatus("error");
      setUploadMessage("Upload failed. Please try again.");
    } finally {
      setIsUploading(false);
      setTimeout(() => setUploadStatus("idle"), 3000);
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
        <p>Drag and drop your script here.</p>
        <span>OR </span>
        <br />
        <label className="browse-button">
          Browse Files
          <input
            type="file"
            ref={fileInput}
            onChange={(e) => setSelectedFile(e.target.files?.[0] || null)}
            hidden
          />
        </label>
      </div>

      {selectedFile && (
        <div className="file-preview">
          <span className="file-name">{selectedFile.name}</span>
          <span className="file-size">
            {(selectedFile.size / 1024).toFixed(2)} KB
          </span>
        </div>
      )}

      <button
        onClick={handleUpload}
        className="upload-button"
        disabled={!selectedFile || isUploading}
      >
        {isUploading ? (
          <>
            <FaSpinner className="spin" />
            Uploading...
          </>
        ) : (
          "Upload Script"
        )}
      </button>

      {uploadStatus !== "idle" && (
        <div className={`status-message ${uploadStatus}`}>{uploadMessage}</div>
      )}
    </div>
  );
};
