import { useRef, useState } from 'react';
import { uploadTestCase } from '../api';

export const TestCaseUpload = () => {
  const [questionId, setQuestionId] = useState('');
  const [testType, setTestType] = useState<'input' | 'output' | 'args'>('input');
  const fileInput = useRef<HTMLInputElement>(null);

  const handleUpload = async () => {
    if (!fileInput.current?.files?.[0]) return;

    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    formData.append('type', 'testcase');
    formData.append('question_id', questionId);
    formData.append('test_type', testType);

    await uploadTestCase(formData);
    window.location.reload();
  };

  return (
    <div className="col-md-8">
      <h5>Upload Test Case</h5>
      <div className="row">
        <div className="col">
          <input
            type="text"
            value={questionId}
            onChange={(e) => setQuestionId(e.target.value)}
            placeholder="Question ID"
            className="form-control"
          />
        </div>
        <div className="col">
          <select
            value={testType}
            onChange={(e) => setTestType(e.target.value as any)}
            className="form-select"
          >
            <option value="input">Input File</option>
            <option value="output">Output File</option>
            {/* <option value="args">Arguments File</option> */}
          </select>
        </div>
        <div className="col">
          <input type="file" ref={fileInput} className="form-control" />
        </div>
        <div className="col">
          <button onClick={handleUpload} className="btn btn-primary">
            Upload
          </button>
        </div>
      </div>
    </div>
  );
};