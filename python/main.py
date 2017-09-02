import RPi.GPIO as GPIO
import dht11
import time
import lcdui
import temperatureTO
import time
import json



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(37, GPIO.OUT) #RED diode
GPIO.setup(35, GPIO.OUT) #WHITE diode

GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) #plus
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) #minus

temperature = 25 #Default temperature is 16 

# read data using pin 7
instance =dht11.DHT11(pin=7)
initFlag = False
debug = False
backlight = True

device = lcdui.lcd(0x3F, 1, backlight, initFlag)
print("Start program")

startTemp = '';

result=instance.read()
if result.is_valid():
      startTemp= int(result.temperature)
      

#main loop
while True:
   button_one = GPIO.input(33)
   if button_one == False:
        temperature = temperature + 1
        print("You increase temperature to", temperature)
   button_two = GPIO.input(31)
   if button_two == False:
        temperature = temperature - 1
        print("You reduces temperature to", temperature)

   #slight pause to debounce
   time.sleep(0.05)   

   result=instance.read()
   if result.is_valid():
      temp = result.temperature
      if startTemp != int(temp):
         device.lcd_puts(str(temp), 1)
         print(json.dumps(temperatureTO.TemperatureTO(time.strftime("%c"),int(temp)))
      if temp > temperature: 
         GPIO.output(37, True)
         GPIO.output(35, False)
      else:
         GPIO.output(37, False)
         GPIO.output(35, True)
   
    

