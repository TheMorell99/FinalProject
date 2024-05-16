class Actuador(object):
    def __init__(self, enclosure):
        """
        Initializes an Actuator object.

        Parameters:
        enclosure (Enclosure): The enclosure object associated with the actuator.

        Returns:
        None
        """
        self.enclosure = enclosure
        
        self.fan = False
        self.gate = False

    
    def set_status(self, value):
        """
        Sets the status of the actuator.

        Args:
            value (str): The status value to set.

        Returns:
            None
        """
        self.value = value


class Fan(Actuador):
    def __init__(self, enclosure):
        """
        Initializes an Actuator object.

        Parameters:
        enclosure (Enclosure): The enclosure object associated with the actuator.
        """
        self.enclosure = enclosure

    def activate(self):
        """
        Activates the actuator by setting the status of the fan to 1.
        """
        self.fan = True

    def deactivate(self):
        """
        Deactivates the actuator by setting the status of the fan to 0.
        """
        self.fan = False


class Gate(Actuador):
    def __init__(self, enclosure):
        """
        Initializes an Actuator object.

        Parameters:
        enclosure (Enclosure): The enclosure object associated with the actuator.
        """
        self.enclosure = enclosure

    def open(self):
        """
        Opens the actuator setting the status of the actuator to 1.
        """
        self.gate = True

    def close(self):
        """
        Close the actuator setting the status of the actuator to 0.
        """
        self.gate = False
