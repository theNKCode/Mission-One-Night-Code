import React from "react";

const OpenPrograms = () => {
  const openProgram = async (endpoint) => {
    try {
      const response = await fetch(`http://localhost:5000/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const result = await response.json();
      alert(result.message);
    } catch (error) {
      alert("Error opening program");
    }
  };

  const openUrl = async () => {
    const url = prompt("Enter URL to open:");
    if (url) {
      try {
        const response = await fetch(`http://localhost:5000/open_url`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ url }),
        });
        const result = await response.json();
        alert(result.message);
      } catch (error) {
        alert("Error opening URL");
      }
    }
  };

  return (
    <div>
      <button onClick={() => openProgram("open_notepad")}>Open Notepad</button>
      <button onClick={() => openProgram("open_vlc")}>Open VLC</button>
      <button onClick={() => openProgram("open_firefox")}>Open Firefox</button>
      <button onClick={openUrl}>Open URL</button>
    </div>
  );
};

export default OpenPrograms;
