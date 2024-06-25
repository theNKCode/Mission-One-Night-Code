import React, { useState } from "react";
import axios from "axios";

function TextToSpeech() {
  const [text, setText] = useState("");
  const [processedText, setProcessedText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:5000/api/process", {
      text,
    });
    setProcessedText(response.data.processed_text);
    speakText(response.data.processed_text);
  };

  const speakText = (text) => {
    if ("speechSynthesis" in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      window.speechSynthesis.speak(utterance);
    } else {
      alert("Speech synthesis is not supported in this browser.");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to speak"
        />
        <button type="submit">Speak</button>
      </form>
      <div>
        <h3>Processed Text:</h3>
        <pre>{processedText}</pre>
      </div>
    </div>
  );
}

export default TextToSpeech;
