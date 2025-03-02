import { useState } from "react";
import {
  FaPlay,
  FaSpinner,
  FaRegClock,
  FaRegCheckCircle,
  FaTimesCircle,
} from "react-icons/fa";
import { runTests } from "../api";
import { ResultsDisplay } from "./ResultsDisplay";
import "./TestControls.css";

interface TestResult {
  Question: string;
  Script: string;
  Test: string;
  Status: "Passed" | "Failed" | "Pending";
  Score: number;
}

export const TestControls = () => {
  const [results, setResults] = useState<TestResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);

  const handleRunTests = async () => {
    try {
      setIsLoading(true);
      setError(null);
      setProgress(0);

      // Simulate progress updates
      const progressInterval = setInterval(() => {
        setProgress((prev) => Math.min(prev + 10, 90));
      }, 500);

      const csvData = await runTests();
      clearInterval(progressInterval);
      setProgress(100);

      const parsedResults = parseCSV(csvData);
      setResults(parsedResults);

      setTimeout(() => setProgress(0), 1000);
    } catch (err) {
      setError(
        "Failed to run tests. Please check your configuration and try again."
      );
      setProgress(0);
    } finally {
      setIsLoading(false);
    }
  };

  const parseCSV = (data: string): TestResult[] => {
    try {
      const lines = data.trim().split("\n");
      const headers = lines[0].split(",").map((h) => h.trim());

      return lines.slice(1).map((line) => {
        const values = line.split(",").map((v) => v.trim());
        return headers.reduce(
          (acc, header, index) => ({
            ...acc,
            [header]:
              header === "Score" ? parseInt(values[index], 10) : values[index],
          }),
          {} as TestResult
        );
      });
    } catch (error) {
      throw new Error("Failed to parse test results");
    }
  };

  return (
    <div className="test-controls-container">
      <div className="controls-header">
        <h3>
          <FaRegClock className="header-icon" />
          Test Execution
        </h3>

        <button
          onClick={handleRunTests}
          className="run-button"
          disabled={isLoading}
        >
          {isLoading ? (
            <>
              <FaSpinner className="spin" />
              Running Tests...
            </>
          ) : (
            <>
              <FaPlay />
              Run All Tests
            </>
          )}
        </button>
      </div>

      {progress > 0 && (
        <div className="progress-container">
          <div className="progress-bar" style={{ width: `${progress}%` }}>
            <span className="progress-text">{progress}%</span>
          </div>
        </div>
      )}

      {error && (
        <div className="error-message">
          <FaTimesCircle />
          {error}
        </div>
      )}

      {results.length > 0 && !isLoading && (
        <div className="success-message">
          <FaRegCheckCircle />
          {results.filter((r) => r.Status === "Passed").length}/{results.length}{" "}
          tests passed
        </div>
      )}

      <ResultsDisplay results={results} />
    </div>
  );
};
