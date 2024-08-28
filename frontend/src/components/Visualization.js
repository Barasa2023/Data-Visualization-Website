// src/components/Visualization.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import API_BASE_URL from '../Config';

function Visualization() {
  const { id } = useParams();
  const [visualization, setVisualization] = useState(null);

  useEffect(() => {
    const fetchVisualization = async () => {
      const response = await fetch(`${API_BASE_URL}/visualization/${id}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setVisualization(data);
      } else {
        alert('Failed to fetch visualization.');
      }
    };

    fetchVisualization();
  }, [id]);

  return (
    <div>
      <h2>Visualization {id}</h2>
      <div>
        {/* Visualization content goes here */}
        {visualization ? (
          <div>{/* Render the visualization */}</div>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default Visualization;