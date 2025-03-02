import { FileManager } from "./components/FileManager";
import { ScriptUpload } from "./components/ScriptUpload";
import { TestCaseUpload } from "./components/TestCaseUpload";
import { TestControls } from "./components/TestControls";
// import { ResultsDisplay } from "./components/ResultsDisplay";
import "./App.css";

export const App = () => {
  return (
    <div className="container mt-5">
      <h1 className="mb-4">Script Tester Dashboard</h1>

      <div className="card mb-4">
        <div className="card-header">Upload Files</div>
        <div className="card-body">
          <div className="row">
            <ScriptUpload />
            <TestCaseUpload />
          </div>
        </div>
      </div>

      <FileManager />
      <TestControls />
      {/* <ResultsDisplay /> */}
    </div>
  );
};
