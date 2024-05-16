import paho.mqtt.client as mqtt        

class Publisher_Mqtt(object):
    def __init__(self) -> None:  
        """
        Initializes the MQTT publisher.

        This method sets up the MQTT client, assigns callback functions for connection and message events,
        and establishes a connection to the MQTT broker.

        Args:
            None

        Returns:
            None
        """
        self.mqttc = mqtt.Client()
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.connect(host='localhost')


    def on_connect(client, userdata, flags, reason_code, properties):
        """
        Callback function that is called when the client successfully connects to the MQTT broker.

        Parameters:
            client (mqtt.Client): The MQTT client instance.
            userdata: The user data that was passed to the client when it was created.
            flags: Response flags sent by the MQTT broker.
            rc (int): The connection result code.

        Returns:
            None

        """
        print(f"Connected with result code {reason_code}")

        
        
    def on_publish(self, client, userdata, msg):
        """
        pass
        """
