from machine import Pin, SoftI2C
import ssd1306
import dht
import time

# ESP32 Pin assignment for OLED
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Initialize the DHT11 sensor on pin 4
sensor = dht.DHT11(Pin(4))

# Loop indefinitely to measure temperature and humidity and display on OLED
while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        
        # Get temperature and humidity values
        temp = sensor.temperature()
        humi = sensor.humidity()
        
        # Display temperature and humidity on OLED
        oled.fill(0) # Clear the display
        oled.text("Temp: {} C".format(temp), 0, 0)
        oled.text("Humidity: {} %".format(humi), 0, 10)
        oled.show() # Refresh the display to show the updated values
        
        # Wait for 1 second between measurements
        time.sleep(1)
        
    except Exception as e:
        print("Error: ", e)
        time.sleep(1)
