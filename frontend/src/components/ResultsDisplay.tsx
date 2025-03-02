import React from "react";
import {
  FaClipboardCheck,
  FaTimesCircle,
  FaQuestionCircle,
  FaFileCode,
  FaChartBar,
} from "react-icons/fa";
import "./ResultsDisplay.css";

interface Result {
  Question: string;
  Script: string;
  Test: string;
  Status: "Passed" | "Failed" | "Pending";
  Score: number;
}

interface ResultsDisplayProps {
  results: Result[];
}

export const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  const getStatusIcon = (status: string) => {
    switch (status) {
      case "Passed":
        return <FaClipboardCheck className="status-icon pass" />;
      case "Failed":
        return <FaTimesCircle className="status-icon fail" />;
      default:
        return <FaQuestionCircle className="status-icon pending" />;
    }
  };

  return (
    <div className="results-card">
      <div className="card-header">
        <FaChartBar className="header-icon" />
        Test Results
        <span className="last-updated">
          Last updated: {new Date().toLocaleTimeString()}
        </span>
      </div>

      <div className="card-body">
        {results.length > 0 ? (
          <div className="table-responsive">
            <table className="results-table">
              <thead>
                <tr>
                  <th className="question-col">
                    <FaQuestionCircle className="column-icon" />
                    Question
                  </th>
                  <th className="script-col">
                    <FaFileCode className="column-icon" />
                    Script
                  </th>
                  <th className="test-col">
                    <FaFileCode className="column-icon" />
                    Test
                  </th>
                  <th className="status-col">Status</th>
                  <th className="score-col">Score</th>
                </tr>
              </thead>
              <tbody>
                {results.map((result, index) => (
                  <tr key={index} className="result-row">
                    <td>{result.Question}</td>
                    <td>{result.Script}</td>
                    <td>{result.Test}</td>
                    <td>
                      <div className="status-container">
                        {getStatusIcon(result.Status)}
                        <span
                          className={`status-text ${result.Status.toLowerCase()}`}
                        >
                          {result.Status}
                        </span>
                      </div>
                    </td>
                    <td>
                      <div className="score-container">
                        <span className="score-value">{result.Score}%</span>
                        <div className="score-bar">
                          <div
                            className="score-progress"
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
