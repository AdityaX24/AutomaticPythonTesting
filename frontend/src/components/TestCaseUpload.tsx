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
  const [inputDragActive, setInputDragActive] = useState(false);
  const [outputDragActive, setOutputDragActive] = useState(false);
  const [inputFile, setInputFile] = useState<File | null>(null);
  const [outputFile, setOutputFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState<
    "idle" | "success" | "error"
  >("idle");
  const [uploadMessage, setUploadMessage] = useState("");
  const [isUploading, setIsUploading] = useState(false);
  const inputFileRef = useRef<HTMLInputElement>(null);
  const outputFileRef = useRef<HTMLInputElement>(null);

  const handleDrag = (
    e: React.DragEvent,
    setDragActive: (active: boolean) => void
  ) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(e.type === "dragenter" || e.type === "dragover");
  };

  const handleDrop = (
    e: React.DragEvent,
    setDragActive: (active: boolean) => void,
    setFile: (file: File | null) => void
  ) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files?.[0]) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!inputFile || !outputFile || !questionId) return;

    setIsUploading(true);
    setUploadStatus("idle");
    setUploadMessage("");

    try {
      const formData = new FormData();
      formData.append("question_id", questionId);
      formData.append("input_file", inputFile);
      formData.append("output_file", outputFile);

      await uploadTestCase(formData);
      setUploadStatus("success");
      setUploadMessage("Test cases uploaded successfully!");
      setInputFile(null);
      setOutputFile(null);
      setQuestionId("");
      if (inputFileRef.current) inputFileRef.current.value = "";
      if (outputFileRef.current) outputFileRef.current.value = "";
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

      <div className="file-upload-sections">
        <div className="form-group">
          <label className="input-label">Input File</label>
          <div
            className={`drag-drop-zone ${inputDragActive ? "active" : ""}`}
            onDragEnter={(e) => handleDrag(e, setInputDragActive)}
            onDragLeave={(e) => handleDrag(e, setInputDragActive)}
            onDragOver={(e) => handleDrag(e, setInputDragActive)}
            onDrop={(e) => handleDrop(e, setInputDragActive, setInputFile)}
          >
            <FaCloudUploadAlt className="upload-icon" />
            <p>Drag and drop input file here</p>
            <span>OR </span>
            <br />
            <label className="browse-button">
              Browse Files
              <input
                type="file"
                ref={inputFileRef}
                onChange={(e) => setInputFile(e.target.files?.[0] || null)}
                hidden
                disabled={isUploading}
              />
            </label>
          </div>
          {inputFile && (
            <div className="file-preview">
              <span className="file-name">{inputFile.name}</span>
              <span className="file-size">
                {(inputFile.size / 1024).toFixed(2)} KB
              </span>
            </div>
          )}
        </div>

        <div className="form-group">
          <label className="input-label">Output File</label>
          <div
            className={`drag-drop-zone ${outputDragActive ? "active" : ""}`}
            onDragEnter={(e) => handleDrag(e, setOutputDragActive)}
            onDragLeave={(e) => handleDrag(e, setOutputDragActive)}
            onDragOver={(e) => handleDrag(e, setOutputDragActive)}
            onDrop={(e) => handleDrop(e, setOutputDragActive, setOutputFile)}
          >
            <FaCloudUploadAlt className="upload-icon" />
            <p>Drag and drop output file here</p>
            <span>OR </span>
            <br />
            <label className="browse-button">
              Browse Files
              <input
                type="file"
                ref={outputFileRef}
                onChange={(e) => setOutputFile(e.target.files?.[0] || null)}
                hidden
                disabled={isUploading}
              />
            </label>
          </div>
          {outputFile && (
            <div className="file-preview">
              <span className="file-name">{outputFile.name}</span>
              <span className="file-size">
                {(outputFile.size / 1024).toFixed(2)} KB
              </span>
            </div>
          )}
        </div>
      </div>

      <button
        onClick={handleUpload}
        className="upload-button"
        disabled={!inputFile || !outputFile || !questionId || isUploading}
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
