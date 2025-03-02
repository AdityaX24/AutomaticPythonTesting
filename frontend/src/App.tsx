// import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Sidebar } from "./components/Sidebar";
import { ScriptUpload } from "./components/ScriptUpload";
import { TestCaseUpload } from "./components/TestCaseUpload";
import { FileManager } from "./components/FileManager";
import { TestControls } from "./components/TestControls";
import "./App.css";

export const App = () => {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="main-content">
          <h1 className="mb-4">Script Tester Dashboard</h1>
          <Routes>
            <Route path="/upload-script" element={<ScriptUpload />} />
            <Route path="/upload-testcase" element={<TestCaseUpload />} />
            <Route path="/delete-files" element={<FileManager />} />
            <Route path="/run-script" element={<TestControls />} />
            <Route path="/" element={<ScriptUpload />} /> {/* Default route */}
          </Routes>
        </div>
      </div>
    </Router>
  );
};
