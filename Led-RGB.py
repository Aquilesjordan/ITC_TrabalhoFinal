import machine, neopixel
import time
from machine import Pin, ADC

n = 1
p = 23
np = neopixel.NeoPixel(machine.Pin(p), n)
x=0
q=1
vet_red=[]
vet_green=[]
vet_blue=[]

while(1):
    print("Color Red")
    while(x<q):
   	 np[0] = (255, 0, 0)
   	 np.write()
   	 time.sleep(1)

   	 ldr = ADC(Pin(33))
   	 ldr.atten(ADC.ATTN_11DB)    
   	 ldr_value = ldr.read()
    	vet_red.append(ldr_value)
   	 x=x+1
    x=0
    print("Color Green")
    while(x<q):
   	 np[0] = (0, 255, 0)
   	 np.write()
   	 time.sleep(1)
    
   	 ldr = ADC(Pin(33))
   	 ldr.atten(ADC.ATTN_11DB)    
   	 ldr_value = ldr.read()
    	vet_green.append(ldr_value)
   	 x=x+1
    x=0
    print("Color Blue")
    while(x<q):
   	 np[0] = (0, 0, 255)
   	 np.write()
   	 time.sleep(1)

   	 ldr = ADC(Pin(33))
   	 ldr.atten(ADC.ATTN_11DB)    
   	 ldr_value = ldr.read()
    	vet_blue.append(ldr_value)
   	 x=x+1
    x=0
    time.sleep(10)
    print(vet_red)
    print(vet_green)
    print(vet_blue)

