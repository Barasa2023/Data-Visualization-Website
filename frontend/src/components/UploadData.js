import React, { useState } from 'react';

function UploadData() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Logic to upload the file to the backend goes here
    console.log('File uploaded:', file);
  };

  return (
    <div>
      <h2>Upload Your Data</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadData;