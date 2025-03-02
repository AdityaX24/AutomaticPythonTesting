import { useRef, useState } from "react";
import {
  FaCloudUploadAlt,
  FaSpinner,
  FaQuestionCircle,
  FaFileCode,
} from "react-icons/fa";
import { uploadTestCase } from "../api";
import "./TestCaseUpload.css";

export const TestCaseUpload = () => {
  const [questionId, setQuestionId] = useState("");
  const [testType, setTestType] = useState<"input" | "output" | "args">(
    "input"
  );
  const [dragActive, setDragActive] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState<
    "idle" | "success" | "error"
  >("idle");
  const [uploadMessage, setUploadMessage] = useState("");
  const [isUploading, setIsUploading] = useState(false);
  const fileInput = useRef<HTMLInputElement>(null);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(e.type === "dragenter" || e.type === "dragover");
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files?.[0]) {
      setSelectedFile(e.dataTransfer.files[0]);
      if (fileInput.current) {
        fileInput.current.files = e.dataTransfer.files;
      }
    }
  };

  const handleUpload = async () => {
    if (!selectedFile || !questionId) return;

    setIsUploading(true);
    setUploadStatus("idle");
    setUploadMessage("");

    try {
      const formData = new FormData();
      formData.append("file", selectedFile);
      formData.append("type", "testcase");
      formData.append("question_id", questionId);
      formData.append("test_type", testType);

      await uploadTestCase(formData);
      setUploadStatus("success");
      setUploadMessage("Test case uploaded successfully!");
      setSelectedFile(null);
      setQuestionId("");
      if (fileInput.current) fileInput.current.value = "";
    } catch (error) {
      setUploadStatus("error");
      setUploadMessage(
        "Upload failed. Please check your inputs and try again."
      );
    } finally {
      setIsUploading(false);
      setTimeout(() => setUploadStatus("idle"), 3000);
    }
  };

  return (
    <div className="testcase-upload-container">
      <h3 className="section-title">
        <FaFileCode className="section-icon" />
        Upload Test Case
      </h3>

      <div className="form-group">
        <label className="input-label">
          <FaQuestionCircle className="input-icon" />
          Question ID
        </label>
        <input
          type="text"
          value={questionId}
          onChange={(e) => setQuestionId(e.target.value)}
          placeholder="Enter question identifier"
          className="form-input"
          disabled={isUploading}
        />
      </div>

      <div className="form-group">
        <label className="input-label">Test Type</label>
        <div className="radio-group">
          {["input", "output"].map((type) => (
            <label key={type} className="radio-label">
              <input
                type="radio"
                value={type}
                checked={testType === type}
                onChange={(e) => setTestType(e.target.value as any)}
                className="radio-input"
                disabled={isUploading}
              />
              <span className="radio-custom"></span>
              {type.charAt(0).toUpperCase() + type.slice(1)}
            </label>
          ))}
        </div>
      </div>

      <div
        className={`drag-drop-zone ${dragActive ? "active" : ""}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <FaCloudUploadAlt className="upload-icon" />
        <p>Drag and drop test case file here</p>
        <span>OR </span>
        <br />
        <label className="browse-button">
          Browse Files
          <input
            type="file"
            ref={fileInput}
            onChange={(e) => setSelectedFile(e.target.files?.[0] || null)}
            hidden
            disabled={isUploading}
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
        disabled={!selectedFile || !questionId || isUploading}
      >
        {isUploading ? (
          <>
            <FaSpinner className="spin" />
            Uploading...
          </>
        ) : (
          "Upload Test Case"
        )}
      </button>

      {uploadStatus !== "idle" && (
        <div className={`status-message ${uploadStatus}`}>{uploadMessage}</div>
      )}
    </div>
  );
};
