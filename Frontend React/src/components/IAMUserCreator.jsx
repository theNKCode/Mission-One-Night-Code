// src/IAMUserCreator.js
import React, { useState } from "react";
import axios from "axios";

const IAMUserCreator = () => {
  const [username, setUsername] = useState("");
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);

  const createUser = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/iamuser", {
        name,
      });
      setUsername(response.data.username);
    } catch (error) {
      console.error("Error creating IAM user:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Create IAM User</h1>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter Username"
      />
      <button onClick={createUser} disabled={loading}>
        {loading ? "Creating..." : "Create User"}
      </button>
      {username && <p>IAM User: {username} created successfully!</p>}
    </div>
  );
};

export default IAMUserCreator;
