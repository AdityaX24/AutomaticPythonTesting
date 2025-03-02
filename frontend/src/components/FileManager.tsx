import { useEffect, useState } from "react";
import { FaTrash, FaFileCode, FaFolder, FaSpinner } from "react-icons/fa";
import { deleteScripts, deleteTestCases, listFiles } from "../api";
import { FileList } from "../types";
import "./FileManager.css";

export const FileManager = () => {
  const [files, setFiles] = useState<FileList>({ scripts: [], questions: [] });
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        setIsLoading(true);
        const data = await listFiles();
        setFiles(data);
        setError(null);
      } catch (err) {
        setError("Failed to load files. Please try again later.");
      } finally {
        setIsLoading(false);
      }
    };
    fetchFiles();
  }, []);

  const handleDelete = async (path: string, type: "script" | "testcase") => {
    if (!window.confirm(`Are you sure you want to delete this ${type}?`))
      return;

    try {
      const deleteFn = type === "script" ? deleteScripts : deleteTestCases;
      await deleteFn(path);
      const updatedFiles = await listFiles();
      setFiles(updatedFiles);
    } catch (err) {
      setError(`Failed to delete ${type}. Please try again.`);
    }
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <FaSpinner className="spin" />
        <span>Loading files...</span>
      </div>
    );
  }

  return (
    <div className="file-manager-card">
      <div className="card-header">
        <FaFolder className="header-icon" />
        File Manager
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="card-body">
        {/* Test Cases Table */}
        <div className="table-section">
          <h5 className="table-title">
            <FaFileCode className="title-icon" />
            Test Cases
          </h5>

          <div className="table-responsive">
            <table className="file-table">
              <thead>
                <tr>
                  <th>Question ID</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {files.questions.map((question) => (
                  <tr key={question}>
                    <td>{question}</td>
                    <td>
                      <button
                        onClick={() =>
                          handleDelete(`questions/${question}`, "testcase")
                        }
                        className="delete-btn"
                      >
                        <FaTrash />
                        <span>Delete</span>
                      </button>
                    </td>
                  </tr>
                ))}
                {files.questions.length === 0 && (
                  <tr className="empty-row">
                    <td colSpan={2}>No test cases found</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>

        {/* Scripts Table */}
        <div className="table-section">
          <h5 className="table-title">
            <FaFileCode className="title-icon" />
            Scripts
          </h5>

          <div className="table-responsive">
            <table className="file-table">
              <thead>
                <tr>
                  <th>File Name</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {files.scripts.map((file) => (
                  <tr key={file}>
                    <td>{file}</td>
                    <td>
                      <button
                        onClick={() =>
                          handleDelete(`scripts/${file}`, "script")
                        }
                        className="delete-btn"
                      >
                        <FaTrash />
                        <span>Delete</span>
                      </button>
                    </td>
                  </tr>
                ))}
                {files.scripts.length === 0 && (
                  <tr className="empty-row">
                    <td colSpan={2}>No scripts found</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};
