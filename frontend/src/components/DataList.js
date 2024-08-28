// src/components/DataList.js
import React, { useState, useEffect } from 'react';
import API_BASE_URL from '../Config';

function DataList() {
  const [dataList, setDataList] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`${API_BASE_URL}/data`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setDataList(data);
      } else {
        alert('Failed to fetch data.');
      }
    };

    fetchData();
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