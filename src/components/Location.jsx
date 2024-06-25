import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function Location() {
  const [location, setLocation] = useState("");
  const [coordinates, setCoordinates] = useState(null);
  const [error, setError] = useState("");

  const handleInputChange = (event) => {
    setLocation(event.target.value);
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/geocode", {
        location,
      });
      setCoordinates(response.data);
      setError("");
    } catch (error) {
      if (error.response) {
        setError(error.response.data.error);
      } else {
        setError("An error occurred");
      }
      setCoordinates(null);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          value={location}
          onChange={handleInputChange}
          placeholder="Enter location"
        />
        <button type="submit">Get Coordinates</button>
      </form>
      {coordinates && (
        <div>
          <p>Latitude: {coordinates.latitude}</p>
          <p>Longitude: {coordinates.longitude}</p>
        </div>
      )}
      {error && <p>{error}</p>}
    </div>
  );
}

export default Location;
