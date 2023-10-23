# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin, I2C
from sh1106 import SH1106_I2C

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
oled = SH1106_I2C(128, 64, i2c, None, addr=0x3C)
oled.sleep(False)


# The following codes should be tested using the REPL.
# #1. To print a string:  
# oled.text('Hello world', 0, 0)
# #2. To display all the commands in queue:     
# oled.show() 
# #3. Now to clear the oled display:  
# oled.fill(0) 
# oled.show() 
# #4. You may also use the invert function to invert the display.  
# oled.invert(1) 
# #5.To display a single pixel.  
# oled.pixel(10,20,1) 
# oled.show() 
# #6. To display a horizontal line  
# oled.hline(30,40,10,1) 
# oled.show() 
# #7. To display a vertical line  
# oled.vline(30,45,5,1) 
# oled.show() 
# #8. While hline and vline is quite useful, there is another function that is more flexible to use which is the line function.  
# oled.line(0,50,10,50,1) 
# oled.show() 
# #9.We may also be able to print a rectangle.  
# oled.rect(10,60,10,5,1) 
# oled.show() 
# #10. Or we may also print a filled rectangle:  
# oled.fill_rect(10,70,10,5,1) 
# oled.show()
