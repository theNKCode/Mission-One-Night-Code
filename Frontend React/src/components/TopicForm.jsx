// src/TopicForm.js
import React, { useState } from "react";
import axios from "axios";

const TopicForm = () => {
  const [topic, setTopic] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/sns", { topic });
      setResponse(res.data);
    } catch (error) {
      console.error("Error creating topic:", error);
      setResponse("Error creating topic");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Topic Name:</label>
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
        </div>
        <button type="submit">Create Topic</button>
      </form>
      {response && <div>Topic ARN: {response}</div>}
    </div>
  );
};

export default TopicForm;
