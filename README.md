<<<<<<< HEAD
# FinalProject
Final project of 'Programació i comunicacions II' 

## UML Diagram
>>>>>>> 549de2e (Adding Readme file)
![diagram](https://github.com/TheMorell99/FinalProject/assets/162160715/fe3f0d25-3a67-4882-af76-bd5c68f4542e)

Farm class represents the printer farm and initializes the TelegramBot class (one to one relation) and one PrinterEnclosure class for every printer (one to meny relation). PrinterEnclouser class is an extension of Enclosure class (can merge both two classes because there's only one type of enclosures). Then, every PrinterEnclosure class initializes three sensors and actuator classes, who are sons of the Sensor and Actuator classes. The Sensor class also initilizes the Publisher_Mqtt class.

## Execution instructions:

1.- Create telegram bot and obtain token and chat_id

2.- Configure config.yaml file with your telegram token, chat id and timer.
  ```
    telegram:
      token: ""
      chat_id: ""
    
    farm:
      timer: 3
  ```

3.- Run mosquitto server (important to run the command with the correct mosquitto.conf). 
  ```
  $ /usr/local/opt/mosquitto/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
  ```

4.- Run the program.
  ```
  $ python3 farm.py --c config.yaml
  ```

5.- Open second terminal to run the mqtt subscriber.
  ```
  $ python3 mqtt_subscriber.py
  ```

6.- Pray that works.



