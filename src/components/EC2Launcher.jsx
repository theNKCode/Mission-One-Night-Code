// src/EC2Launcher.js
import React, { useState } from "react";
import axios from "axios";

const EC2Launcher = () => {
  const [instanceId, setInstanceId] = useState("");
  const [loading, setLoading] = useState(false);

  const launchInstance = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://localhost:5000/ec2");
      setInstanceId(response.data.instance_id);
    } catch (error) {
      console.error("Error launching instance:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Launch EC2 Instance</h1>
      <button onClick={launchInstance} disabled={loading}>
        {loading ? "Launching..." : "Launch Instance"}
      </button>
      {instanceId && <p>Instance ID: {instanceId}</p>}
    </div>
  );
};

export default EC2Launcher;
