import React from "react";
import { FaClipboardCheck, FaChartBar, FaFileExcel } from "react-icons/fa";
import "./ResultsDisplay.css";

interface Result {
  Question: string;
  Script_Name: string;
  SRN_1: string;
  SRN_2: string;
  PassedTests: number;
  TotalTests: number;
  Score: number;
}

interface ResultsDisplayProps {
  results: Result[];
}

export const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  const handleDownloadExcel = async () => {
    try {
      const response = await fetch("http://localhost:8000/download-excel");
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `test_results_${new Date().toISOString().slice(0, 10)}.xlsx`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Download failed:", error);
    }
  };

  return (
    <div className="results-card">
      <div className="card-header">
        <div className="header-left">
          <FaChartBar className="header-icon" />
          Test Results ({results.length} submissions)
        </div>
        <div className="header-right">
          <button onClick={handleDownloadExcel} className="download-button">
            <FaFileExcel className="download-icon" />
            Download Excel
          </button>
          <span className="last-updated">
            Last updated: {new Date().toLocaleTimeString()}
          </span>
        </div>
      </div>

      <div className="card-body">
        {results.length > 0 ? (
          <div className="table-container">
            <table className="results-table">
              <thead>
                <tr>
                  <th>Question</th>
                  <th>Script Name</th>
                  <th>SRN 1</th>
                  <th>SRN 2</th>
                  <th>Passed</th>
                  <th>Total</th>
                  <th>Score</th>
                </tr>
              </thead>
              <tbody>
                {results.map((result, index) => (
                  <tr key={index}>
                    <td>{result.Question}</td>
                    <td>{result.Script_Name}</td>
                    <td>{result.SRN_1}</td>
                    <td>{result.SRN_2}</td>
                    <td>{result.PassedTests}</td>
                    <td>{result.TotalTests}</td>
                    <td>
                      <div className="score-display">
                        <div className="score-text">
                          {result.Score.toFixed(2)}%
                        </div>
                        <div className="score-bar-container">
                          <div
                            className="score-bar-fill"
                            style={{ width: `${result.Score}%` }}
                          ></div>
                        </div>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="empty-state">
            <FaClipboardCheck className="empty-icon" />
            <p>No test results available</p>
            <small>Run tests to see results here</small>
          </div>
        )}
      </div>
    </div>
  );
};
