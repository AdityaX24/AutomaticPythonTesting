import { useEffect, useState } from "react";
import { deleteScripts, deleteTestCases, listFiles } from "../api";
import { FileList } from "../types";

export const FileManager = () => {
  const [files, setFiles] = useState<FileList>({ scripts: [], questions: [] });

  useEffect(() => {
    const fetchFiles = async () => {
      const data = await listFiles();
      setFiles(data);
    };
    fetchFiles();
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-header">File Manager</div>
      <div className="card-body">
        <div className="row">
          <div className="col-md-6">
            <h5>Scripts</h5>
            <div className="list-group">
              {files.scripts.map((file) => (
                <div
                  key={file}
                  className="list-group-item d-flex justify-content-between"
                >
                  {file}
                  <button
                    onClick={async () => {
                      try {
                        await deleteScripts(`scripts/${file}`); // Call the delete function
                        window.location.reload(); // Reload the page after deletion
                      } catch (error) {
                        console.error("Error deleting file:", error);
                        // Optionally, show an error message to the user
                      }
                    }}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </div>
              ))}
            </div>
          </div>
          <div className="col-md-6">
            <h5>Test Cases</h5>
            <div className="list-group">
              {files.questions.map((question) => (
                <div key={question} className="list-group-item">
                  <strong>{question}</strong>
                  <button
                    onClick={async () => {
                      try {
                        await deleteTestCases(`questions/${question}`); // Call the delete function
                        window.location.reload(); // Reload the page after deletion
                      } catch (error) {
                        console.error("Error deleting file:", error);
                        // Optionally, show an error message to the user
                      }
                    }}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
