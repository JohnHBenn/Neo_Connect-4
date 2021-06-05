import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()

def setup():
    global red
    global blue
    global color
    trellis.pixels.fill(clear)

red = (20,0,0)
blue = (0,0,20)
clear = (0,0,0)
color = red

a = (0,0)
b = (1,0)
c = (2,0)
d = (3,0)
e = (4,0)
f = (5,0)
g = (6,0)
h = (7,0)
aa = (0,1)
ab = (1,1)
ac = (2,1)
ad = (3,1)
ae = (4,1)
af = (5,1)
ag = (6,1)
ah = (7,1)
ba = (0,2)
bb = (1,2)
bc = (2,2)
bd = (3,2)
be = (4,2)
bf = (5,2)
bg = (6,2)
bh = (7,2)
ca = (0,3)
cb = (1,3)
cc = (2,3)
cd = (3,3)
ce = (4,3)
cf = (5,3)
cg = (6,3)
ch = (7,3)

soln = [[a,b,c,d],[b,c,d,e],[c,d,e,f],[d,e,f,g],[e,f,g,h],[aa,ab,ac,ad],[ab,ac,ad,ae],[ac,ad,ae,af],[ad,ae,af,ag],[ae,af,ag,ah],[ba,bb,bc,bd],[bb,bc,bd,be],[bc,bd,be,bf],[bd,be,bf,bg],[be,bf,bg,bh],[ca,cb,cc,cd],[cb,cc,cd,ce],[cc,cd,ce,cf],[cd,ce,cf,cg],[ce,cf,cg,ch],[a,aa,ba,ca],[b,ab,bb,cb],[c,ac,bc,cc],[d,ad,bd,cd],[e,ae,be,ce],[f,af,bf,cf],[g,ag,bg,cg],[h,ah,bh,ch],[a,ab,bc,cd],[b,ac,bd,ce],[c,ad,be,cf],[d,ae,bf,cg],[e,af,bg,ch],[h,ag,bf,ce],[g,af,be,cd],[f,ae,bd,cc],[e,ad,bc,cb],[d,ac,bb,ca]]
setup()
while True:

    pressed = set(trellis.pressed_keys)    
    
    for press in pressed:
        if press:
        
            x, y = press
            if trellis.pixels[x,y] == (0,0,0):
                trellis.pixels[x,y] = color
                if color == red:
                    color = blue
                elif color == blue :
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

    for i in range(38):
        if trellis.pixels[soln[i][0]] == red and trellis.pixels[soln[i][1]] == red and trellis.pixels[soln[i][2]] == red and trellis.pixels[soln[i][3]] == red:
            trellis.pixels.fill(red)
            time.sleep(1)
            setup()
        if trellis.pixels[soln[i][0]] == blue and trellis.pixels[soln[i][1]] == blue and trellis.pixels[soln[i][2]] == blue and trellis.pixels[soln[i][3]] == blue:
            trellis.pixels.fill(blue)
            time.sleep(1)
            setup()
