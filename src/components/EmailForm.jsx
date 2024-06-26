import React, { useState } from "react";
import axios from "axios";

const EmailForm = () => {
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/snsemail", {
        subject,
        message,
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Error sending email:", error);
      setResponse("Error sending email");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Subject:</label>
          <input
            type="text"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
          />
        </div>
        <div>
          <label>Message:</label>
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <button type="submit">Send Email</button>
      </form>
      {response && <div>Response: {response}</div>}
    </div>
  );
};

export default EmailForm;
