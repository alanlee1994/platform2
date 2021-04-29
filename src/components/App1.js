import React from 'react';
// import Paho from 'paho-mqtt';
import Paho from 'paho-mqtt';
import { Signal } from "../protobuf/signal_pb";
import NavBar from './NavBar';
import DataTable from './Display';
import 'semantic-ui-css/semantic.min.css';

function App() {
  const [msgArray, setMsgArray] = React.useState([]);
  const [client, setClient] = React.useState(null);

  React.useEffect(() => {
    _init();
    console.log('initialised')
  }, [])

  const _init = () => {
    const clientID = "web" + new Date().getTime(); 
    const c = new Paho.Client("rabbitmq", 15675, "/ws", clientID);
    setClient(c);
  }
  
  var options = {
    userName: "eon_dev:eon_dev",
    password: "eon_dev",
    onSuccess: onConnect,
    onFailure: doFail
  };

 
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    // console.log("onConnect"); 
    var sub_options = {
      onSuccess: onConnectSub,
      onFailure: doFailSub
    }
    client.subscribe("#", sub_options);
  }
  function onConnectSub(msg){
    // console.log("connected and subscripting: " + JSON.stringify(msg));
  }
  function doFailSub(a, code,msg){
    
  }
  function doFail(e){
    console.log(e);
  }
    
  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+ responseObject.errorMessage);
    }
  }
  // called when a message arrives

  function onMessageArrived(message) {
    const decodedMessage = Signal.deserializeBinary(message.payloadBytes);
    const signalName = decodedMessage.getName()
    const signalInstrument = decodedMessage.getInstruments()
    const signalTs = decodedMessage.getSignalTs()
    // const signalStats = decodedMessage.getStatsList()
    // console.log(signalName, signalInstrument, signalTs)
    // console.log(decodedMessage)
    let receivedMsg = {signalName: signalName,       
                                    signalInstrument: signalInstrument, 
                                    signalTs: signalTs};
    
    setMsgArray(msgArray.concat(receivedMsg));
  }

  // connect the client
  if (client !== null){
    client.connect(options);
    // called when the client connects
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    // console.log(msgArray);
  }
  
    
  return (
    <div>
      <NavBar/>
      <DataTable data={msgArray}/>
    </div>
  );
}

export default App;
