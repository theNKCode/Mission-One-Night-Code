// src/VolumeCreator.js
import React, { useState } from "react";
import axios from "axios";

const VolumeCreator = () => {
  const [volumeId, setVolumeId] = useState("");
  const [size, setSize] = useState("");
  const [loading, setLoading] = useState(false);

  const createVolume = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/volume", {
        size,
      });
      setVolumeId(response.data.volume_id);
    } catch (error) {
      console.error("Error creating volume:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Create Volume</h1>
      <input
        type="number"
        value={size}
        onChange={(e) => setSize(e.target.value)}
        placeholder="Enter Volume Size"
      />
      <button onClick={createVolume} disabled={loading}>
        {loading ? "Creating..." : "Create Volume"}
      </button>
      {volumeId && <p>Volume ID: {volumeId}</p>}
    </div>
  );
};

export default VolumeCreator;
