import Paho from 'paho-mqtt';


const clientID = "web" + new Date().getTime(); 
var client = new Paho.Client("rabbitmq", 15675, "/ws", clientID);

export default client;