import paho.mqtt.client as mqtt


class Subscriber_Mqtt:
    def __init__(self) -> None:
        """
            Initializes an instance of the MQTTSubscriber class.

            The MQTTSubscriber class is responsible for subscribing to MQTT topics and handling incoming messages.

            Args:
                None

            Returns:
                None
        """
        mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        mqttc.connect("localhost")
        mqttc.loop_forever()


    def on_connect(self, client, userdata, flags, reason_code, properties):
        """
            Callback function that is called when the client connects to the MQTT broker.

            Parameters:
            - client: The MQTT client instance that triggered the callback.
            - userdata: Any user-defined data that was passed to the client when it was created.
            - flags: A dictionary containing flags associated with the connection.
            - rc: The result code returned by the MQTT broker.

            Returns:
            None
        """
        print(f"Connected with result code {reason_code}")
        client.subscribe("#")

    def on_message(self, client, userdata, msg):
        """
            Callback function that is called when a new message is received.

            Args:
                client: The MQTT client instance that received the message.
                userdata: Any user-defined data that was passed to the MQTT client.
                msg: The MQTT message object containing the topic and payload.

            Returns:
                None

            """
        print(msg.topic+" "+str(msg.payload))


# Main program
if __name__ == "__main__":
    # Initialize class
    subscriber = Subscriber_Mqtt()
        
        

