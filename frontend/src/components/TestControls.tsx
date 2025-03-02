import { useState } from "react";
import { runTests } from "../api";
import { ResultsDisplay } from "./ResultsDisplay";

export const TestControls = () => {
  const [results, setResults] = useState<any[]>([]);
  const handleRunTests = async () => {
    const csvData = await runTests();
    const parsedResults = parseCSV(csvData); // Parse the CSV data
    setResults(parsedResults); // Update state with parsed results
  };

  const parseCSV = (data: string) => {
    const lines = data.trim().split("\n");
    const headers = lines[0].split(",");
    return lines.slice(1).map((line) => {
      const values = line.split(",");
      return headers.reduce((acc, header, index) => {
        acc[header.trim()] = values[index].trim();
        return acc;
      }, {} as any);
    });
  };

  return (
    <>
      <button onClick={handleRunTests} className="btn btn-success mb-4">
        Run All Tests
      </button>
      <ResultsDisplay results={results} />{" "}
      {/* Pass results to ResultsDisplay */}
    </>
  );
};
