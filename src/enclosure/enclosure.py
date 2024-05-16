from .sensors import TemperatureSensor, HumiditySensor, FilamentRunOut
from .actuator import Fan, Gate

class Enclosure(object):

    def __init__(self, farm, id):
        """
        Initializes an instance of the Enclosure class.

        Args:
            farm: The Farm object that the enclosure belongs to.
            id (int): The unique identifier for the enclosure.

        Attributes:
            id (int): The unique identifier for the enclosure.
            farm (Farm): The Farm object that the enclosure belongs to.
            bot (Bot): The Bot object associated with the farm.
            enclosure_type (str): The type of the enclosure ("printerEnclosure" or "filamentEnclosure").
            fan (Fan): The Fan object associated with the enclosure.
            gate (Gate): The Gate object associated with the enclosure.
        """

        self.farm = farm
        self.id = id
        self.enclosure_type = PrinterEnclosure(self, id) # Args: Enclosure() class and printer id
        self.fan = Fan(self) # Args: Enclosure() class
        self.gate = Gate(self) # Args: Enclosure() class

    
    def get_enclosure_id(self):
        """
        Returns the ID of the enclosure.

        Returns:
            int: The ID of the enclosure.
        """
        return self.id

    
    
    def activate_fan(self):
        """
        Activates the fan of the enclosure.

        This method sends a message to the bot indicating the ID of the enclosure and the type of fan being activated.
        It then calls the `activate` method of the fan object to activate the fan.

        Parameters:
        None

        Returns:
        None
        """
        self.farm.bot.sendMessage(f"Fan is being activated on printer id: {self.id}.")
        self.fan.activate()
    
    
    def deactivate_fan(self):
        """
        Deactivates the fan in the enclosure.

        Sends a message indicating the ID and type of the enclosure fan being deactivated,
        and then calls the `deactivate` method of the fan object.
        """
        self.farm.bot.sendMessage(f"Fan is being deactivated of printer id: {self.id}.")
        self.fan.deactivate()

    
    
    def open_gate(self):
        """
        Opens the gate of the enclosure.

        This method sends a message indicating the ID and type of the enclosure gate being opened,
        and then opens the gate.
        """
        self.farm.bot.sendMessage(f"Gate is being opened on printer id: {self.id}.") 
        self.gate.open()

   
   
    def close_gate(self):
        """
        Closes the gate of the enclosure.

        This method sends a message to the bot indicating that the gate is being closed,
        and then closes the gate.

        Parameters:
        - None

        Returns:
        - None
        """
        self.farm.bot.sendMessage(f"Gate is being closed on printer id: {self.id}.") 
        self.gate.close()

    
    
    def temperature_notification(self, value):
        """
        Sends a temperature notification message.

        Args:
            value (float): The temperature value in degrees Celsius.

        Returns:
            None
        """
        self.farm.bot.sendMessage(f"Temperature on printer id: {self.id} is {value}ºC") 
        


    def humidity_notification(self, value):
        """
        Sends a notification when the humidity level is too high.

        Parameters:
        - value (float): The humidity level in percentage.

        Returns:
        None
        """
        self.farm.bot.sendMessage(f"Humidity of printer id: {self.id} is {value}%. Value too high!") 
        
    


    def filament_notification(self, value):
        """
        Sends a notification when the filament runs out.

        This method sends a notification with the ID of the enclosure and a message indicating that the filament has run out.
        """
        self.farm.bot.sendMessage(f"Filament of printer id: {self.id} has run out.") 
        

    

    def loop_once(self):
        """
        Perform one iteration of the enclosure loop.

        This method generates data for every sensor, checks the readings, sends them via MQTT,
        and activates or opens the corresponding fan or gate.
        """
       
        
        for sensor in self.enclosure_type.sensors:
                """
                Here we iterate on every sensor from the PrinterEnclosure() class.
                We call the corresponding methods to read, check and send data.
                The random method will generate the random data for every sensor.
                The check method will modify the gate and fan values.
                """
                sensor.random()
                sensor.check()
                
            

        
        




class PrinterEnclosure(Enclosure):
    def __init__(self, enclosure, id):
        """
        Initializes an instance of the Enclosure class.

        Args:
            farm (Farm): The farm object to which the enclosure belongs.
            id (int): The unique identifier for the enclosure.

        Attributes:
            sensors (list): A list of sensors attached to the enclosure.

        """
        
    
        self.sensors = [
            TemperatureSensor(enclosure, id), # Args: Enclosure() class and printer id
            HumiditySensor(enclosure, id), # Args: Enclosure() class and printer id
            FilamentRunOut(enclosure, id), # Args: Enclosure() class and printer id
        ]


            