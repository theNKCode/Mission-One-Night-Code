import React from "react";
import Location from "../src/components/Location";
import WhatsApp from "../src/components/WhatsApp";
import TextToSpeech from "../src/components/TextToSpeech";
import OpenPrograms from "../src/components/OpenPrograms";
import "./Styles.css";

function App() {
  return (
    <>
      <Location />
      <WhatsApp />
      <TextToSpeech />
      <div className="App">
        <header className="App-header">
          <h1>Open Programs</h1>
          <OpenPrograms />
        </header>
      </div>
    </>
  );
}

export default App;
