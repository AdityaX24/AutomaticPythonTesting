import { useRef } from 'react';
import { uploadScript } from '../api';

export const ScriptUpload = () => {
  const fileInput = useRef<HTMLInputElement>(null);

  const handleUpload = async () => {
    if (!fileInput.current?.files?.[0]) return;
    
    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    formData.append('type', 'script');
    
    await uploadScript(formData);
    window.location.reload();
  };

  return (
    <div className="col-md-4">
      <h5>Upload Script</h5>
      <input type="file" ref={fileInput} className="form-control" />
      <button onClick={handleUpload} className="btn btn-primary mt-2">
        Upload
      </button>
    </div>
  );
};