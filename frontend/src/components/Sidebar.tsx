import React from "react";
import { Link } from "react-router-dom";
import "./Sidebar.css";

export const Sidebar = () => {
  return (
    <div className="sidebar">
      <ul>
        <li>
          <Link to="/upload-script">Upload Script</Link>
        </li>
        <li>
          <Link to="/upload-testcase">Upload Test Case</Link>
        </li>
        <li>
          <Link to="/delete-files">Delete Files</Link>
        </li>
        <li>
          <Link to="/run-script">Run Script</Link>
        </li>
      </ul>
    </div>
  );
};
