// import React from "react";
import { Link } from "react-router-dom";
import { FaUpload, FaFileImport, FaTrash, FaPlayCircle } from "react-icons/fa";
import "./Sidebar.css";

export const Sidebar = () => {
  return (
    <div className="sidebar">
      <ul>
        <li>
          <Link to="/upload-script" className="sidebar-link">
            <FaUpload className="sidebar-icon" />
            <span>Upload Script</span>
          </Link>
        </li>
        <li>
          <Link to="/upload-testcase" className="sidebar-link">
            <FaFileImport className="sidebar-icon" />
            <span>Upload Test Case</span>
          </Link>
        </li>
        <li>
          <Link to="/delete-files" className="sidebar-link">
            <FaTrash className="sidebar-icon" />
            <span>Delete Files</span>
          </Link>
        </li>
        <li>
          <Link to="/run-script" className="sidebar-link">
            <FaPlayCircle className="sidebar-icon" />
            <span>Run Script</span>
          </Link>
        </li>
      </ul>
    </div>
  );
};
