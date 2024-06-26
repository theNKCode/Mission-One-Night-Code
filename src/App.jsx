import React from "react";
import Location from "../src/components/Location";
import WhatsApp from "../src/components/WhatsApp";
import TextToSpeech from "../src/components/TextToSpeech";
import OpenPrograms from "../src/components/OpenPrograms";
import "./Styles.css";
import TopicForm from "./components/TopicForm";
import EmailForm from "./components/EmailForm";
import EC2Launcher from "./components/EC2Launcher";
import VolumeCreator from "./components/VolumeCreator";
import IAMUserCreator from "./components/IAMUserCreator";
import BucketCreator from "./components/BucketCreator";
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
      <div className="App">
        <header className="App-header">
          <EC2Launcher />
        </header>
      </div>
      <div className="App">
        <header className="App-header">
          <VolumeCreator />
        </header>
      </div>
      <div className="App">
        <header className="App-header">
          <IAMUserCreator />
        </header>
      </div>
      <div className="App">
        <header className="App-header">
          <BucketCreator />
        </header>
      </div>
    </>
  );
}

export default App;
