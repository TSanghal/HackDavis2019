#import Adafruit libraries
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
#create spi
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
#create chip select
cs = digitalio.DigitalInOut(board.D5)
 
#create the mcp device object
mcp = MCP.MCP3008(spi, cs)
 
#create an analog input channel on pin 0
channel = AnalogIn(mcp, MCP.P0)

while True:
    print('Raw ADC Value: ', channel.value)
    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    time.sleep(0.5)
