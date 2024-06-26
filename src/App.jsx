import React from "react";
import Location from "../src/components/Location";
import WhatsApp from "../src/components/WhatsApp";
import TextToSpeech from "../src/components/TextToSpeech";
import OpenPrograms from "../src/components/OpenPrograms";
import "./Styles.css";
import TopicForm from "./components/TopicForm";
import EmailForm from "./components/EmailForm";

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
      {/* <div className="App">
        <header className="App-header">
          <h1>SNS Topic Creator</h1>
        </header>
        <TopicForm />
      </div> */}
      <TopicForm />
      <EmailForm />
      {/* <CreateEc2 /> */}
    </>
  );
}

export default App;
