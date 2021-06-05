import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()

red = (20,0,0)
blue = (0,0,20)
color = red

while True:
   
    pressed = set(trellis.pressed_keys)
    
    for press in pressed:
        if press:
            x, y = press
            if trellis.pixels[x,y] = (0,0,0):
               trellis.pixels[x,y] = color
               if color == red:
                   color = blue
               elif color == blue:
                   color = red
        
    
    for i in range(8):
        if trellis.pixels[i, 0] != (0, 0, 0) and trellis.pixels[i, 1] == (0, 0,0):
            drop_color= trellis.pixels[i, 0]
            time.sleep(.5)
            trellis.pixels[i, 0] = (0, 0, 0)
            trellis.pixels[i, 1] = (drop_color)
        
        if trellis.pixels[i, 1] != (0, 0, 0) and trellis.pixels[i, 2] == (0, 0,0):
            drop_color= trellis.pixels[i, 1]
            time.sleep(.5)
            trellis.pixels[i, 1] = (0, 0, 0)
            trellis.pixels[i, 2] = (drop_color)
            
            
        if trellis.pixels[i, 2] != (0, 0, 0) and trellis.pixels[i, 3] == (0, 0,0):
            drop_color= trellis.pixels[i, 2]
            time.sleep(.5)
            trellis.pixels[i, 2] = (0, 0, 0)
            trellis.pixels[i, 3] = (drop_color)
