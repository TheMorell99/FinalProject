from mqtt.mqtt_publisher import Publisher_Mqtt
import random

class Sensor(object):
    def __init__(self, enclosure):
        """
        Initializes a Sensors object.

        Args:
            enclosure: The enclosure object associated with the sensors.

        Attributes:
            publisher: An instance of the Publisher_Mqtt class.
            lecture: An integer representing the initial lecture value (99999 in this case).
            enclosure: The enclosure object associated with the sensors.
        """
        
        self.publisher = Publisher_Mqtt()
        self.lecture = 99999
        self.enclosure = enclosure
        


    def publish_message(self, topic, value): 
        """
        Publishes a message via MQTT.

        Args:
            topic (str): The topic to publish the message to.
            value: The value to be published.

        Returns:
            None
        """
        self.publisher.mqttc.publish(topic, value)
        


class TemperatureSensor(Sensor):
    def __init__(self, enclosure, id):
        """
        Initializes a new instance of the Sensors class.

        Args:
            enclosure: The enclosure object associated with the sensors.

        Returns:
            None
        """
        self.id = id
        super().__init__(enclosure)

       
        
        
        
    def random(self):
        """Generate random data simulating sensor lecture
        
        This method generates a random value between 20 and 50 to simulate a sensor lecture.
        The generated value is stored in the `lecture` attribute of the object.
        """
        self.lecture = random.randint(20, 50) # both included
    

    def send(self):
        """Send the last lecture and message of the sensor to the broker via mqtt.

        This method publishes the temperature lecture of the sensor to the MQTT broker.
        The topic is constructed using the enclosure ID and the sensor's lecture value.
        """
        self.publish_message(f"/sensors/temperature/{self.id}", self.lecture)
        
       
    

    def check(self):
        """
        Checks the lecture value and performs actions based on its value.

        If the lecture value is greater than 45, it is considered a high lecture. In this case,
        if the publisher is successfully connected to the broker, the lecture is sent via MQTT.
        The temperature notification is also sent to the enclosure and the fan is activated.

        If the lecture value is between 20 and 45 (inclusive), it is considered a normal lecture.
        In this case, if the publisher is successfully connected to the broker, the lecture is sent via MQTT.

        If the lecture value is less than 20, it is considered an error with the lecture. In this case,
        the lecture value is set to 99999. If the publisher is successfully connected to the broker,
        the lecture is sent via MQTT.

        """
        if self.lecture > 45:
            self.send()
            # TODO: Activate fan
            self.enclosure.temperature_notification(self.lecture)
            self.enclosure.activate_fan()
        elif self.lecture >= 20 and self.lecture <= 45:
            self.send()
        else:
            self.lecture = 99999
            self.send()


class HumiditySensor(Sensor):
    def __init__(self, enclosure, id):
        """
        Initializes a new instance of the Sensors class.

        Args:
            enclosure (Enclosure): The enclosure object associated with the sensors.

        Returns:
            None
        """
        self.id = id
        super().__init__(enclosure)
        


    def random(self):
        """Generate random data simulating sensor lecture
        
        This method generates a random value between 0 and 100 to simulate a sensor lecture.
        The generated value is stored in the `lecture` attribute of the object.
        """
        self.lecture = random.randint(0, 100) # both included
        


    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt.

        This method publishes the last lecture and message of the sensor to the broker
        using the MQTT protocol. The topic used for publishing is dynamically generated
        based on the enclosure ID of the sensor.

        Args:
            None

        Returns:
            None
        """
        self.publish_message(f"/sensors/humidity/{self.id}", self.lecture)
       



    def check(self):
        """
        Checks the lecture value and performs actions based on its value.

        If the lecture value is greater than 95, it is considered a high lecture. In this case,
        if the publisher is successfully connected to the broker, the lecture is sent via MQTT.
        The HumidityNotification method of the enclosure is called with the lecture value, and
        the gate is opened.

        If the lecture value is between 0 and 95 (inclusive), it is considered a normal lecture.
        In this case, if the publisher is successfully connected to the broker, the lecture is
        sent via MQTT.

        If the lecture value is less than 0, it is considered an error. In this case, the lecture
        value is set to 99999. If the publisher is successfully connected to the broker, the
        lecture is sent via MQTT.

        """
        if self.lecture > 95:
            # TODO: HuidityNotification() method from enclosure
            self.enclosure.humidity_notification(self.lecture)
            self.send()
        elif self.lecture >= 0 and self.lecture <= 95:
            self.send()
        else: 
            self.lecture = 99999
            self.send()







class FilamentRunOut(Sensor):
    def __init__(self, enclosure, id):
        """
        Initializes a new instance of the Sensors class.

        Args:
            enclosure (Enclosure): The enclosure object associated with the sensors.

        Returns:
            None
        """
        
        super().__init__(enclosure)
        self.id = id


    def random(self):
        """Generate random data simulating sensor lecture.

        This method generates a random sensor lecture value between 0 and 100.
        If the lecture value is greater than or equal to 95, it sets the lecture
        attribute to EMPTY. Otherwise, it sets the lecture attribute
        to NOT_EMPTY.

        """
        if random.randint(0, 100) >= 95:
            self.lecture = "EMPTY"
        else:
            self.lecture = "NO_EMPTY"




    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt.

        This method publishes the last lecture and message of the sensor to the broker
        using the MQTT protocol. The topic used for publishing is dynamically generated
        based on the enclosure ID and the sensor's status.

        Args:
            None

        Returns:
            None
        """
        self.publish_message(f"/sensors/filament/{self.id}", self.lecture)



    def check(self):
        """
        Checks the sensor lecture and performs actions based on the lecture value.

        If the lecture is EMPTY, it sends the lecture via MQTT if successfully connected to the broker
        and runs the runOutNotification method of the enclosure.

        If the lecture is NOT_EMPTY, it sends the lecture via MQTT if successfully connected to the broker.

        If the lecture is neither EMPTY nor NOT_EMPTY, it sets the lecture value to 99999 and
        sends the lecture via MQTT if successfully connected to the broker.
        """
        if self.lecture == "EMPTY":
            # TODO: runOutNotification() method of the enclosure
            self.enclosure.filament_notification(self.lecture)
            self.send()
        elif self.lecture == "NOT_EMPTY":
            self.send()
        else:
            self.lecture = 99999
            self.send()
