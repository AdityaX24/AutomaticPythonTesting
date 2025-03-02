import React from "react";

interface Result {
  Question: string;
  Script: string;
  Test: string;
  Status: string;
  Score: string;
}

interface ResultsDisplayProps {
  results: Result[];
}

export const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  return (
    <div className="card">
      <div className="card-header">Test Results</div>
      <div className="card-body">
        {results.length > 0 ? (
          <table className="table">
            <thead>
              <tr>
                <th>Question</th>
                <th>Script</th>
                <th>Test</th>
                <th>Status</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => (
                <tr key={index}>
                  <td>{result.Question}</td>
                  <td>{result.Script}</td>
                  <td>{result.Test}</td>
                  <td>{result.Status}</td>
                  <td>{result.Score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No results available.</p>
        )}
      </div>
    </div>
  );
};
