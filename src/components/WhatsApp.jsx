import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function WhatsApp() {
  const [phoneNumber, setPhoneNumber] = useState("");
  const [message, setMessage] = useState("");
  const [hour, setHour] = useState("");
  const [minute, setMinute] = useState("");
  const [response, setResponse] = useState("");

  const handleInstantSubmit = async (event) => {
    event.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/send_instant", {
        phone_number: phoneNumber,
        message: message,
      });
      setResponse(res.data.status || res.data.error);
    } catch (error) {
      setResponse(error.message);
    }
  };

  const handleScheduledSubmit = async (event) => {
    event.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/send_scheduled", {
        phone_number: phoneNumber,
        message: message,
        hour: parseInt(hour),
        minute: parseInt(minute),
      });
      setResponse(res.data.status || res.data.error);
    } catch (error) {
      setResponse(error.message);
    }
  };

  return (
    <div className="App">
      <h1>WhatsApp Message Sender</h1>
      <form onSubmit={handleInstantSubmit}>
        <h2>Send Instant Message</h2>
        <input
          type="text"
          placeholder="Phone Number"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
        <input
          type="text"
          placeholder="Message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Send Instant</button>
      </form>

      <form onSubmit={handleScheduledSubmit}>
        <h2>Send Scheduled Message</h2>
        <input
          type="text"
          placeholder="Phone Number"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
        <input
          type="text"
          placeholder="Message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <input
          type="number"
          placeholder="Hour"
          value={hour}
          onChange={(e) => setHour(e.target.value)}
        />
        <input
          type="number"
          placeholder="Minute"
          value={minute}
          onChange={(e) => setMinute(e.target.value)}
        />
        <button type="submit">Send Scheduled</button>
      </form>

      {response && <p>{response}</p>}
    </div>
  );
}

export default WhatsApp;
