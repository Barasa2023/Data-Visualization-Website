import React, { useState, useEffect } from 'react';

function DataList() {
  const [dataList, setDataList] = useState([]);

  useEffect(() => {
    // Logic to fetch the list of data from the backend goes here
    setDataList([
      { id: 1, name: 'Dataset 1' },
      { id: 2, name: 'Dataset 2' },
    ]);
  }, []);

  return (
    <div>
      <h2>Manage Your Data</h2>
      <ul>
        {dataList.map(data => (
          <li key={data.id}>{data.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default DataList;