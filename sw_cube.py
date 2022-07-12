#!/usr/bin/python

# This is the "neocube" script "sw_cube.py" based on the python port "cubebit.py".
# The python script works on all newer Raspberry Pi (2/3/4/B/+), RPi Zero 1/2 
# with the "cubebit.py" python port for slices based on 4tronix neopixel cubes.
# It's just a sample to demo what's possible under use of our development "swc.py".
# "swc.py" is our own class symplifing squares and cubes.

# author        : Swen Hopfe
# created       : 22-01-10
# last modified : 22-02-18

#--------------------------------------------------------------------------------

import cubebit as cb
import swc as cbs
import time
import random

side = 5
brightness = 14
cb.create(side,brightness)
cbs.init(side)

black  = cb.fromRGB(0,0,0)
white  = cb.fromRGB(90,90,90)
grey1  = cb.fromRGB(40,40,55)
grey2  = cb.fromRGB(10,10,25)
yellow = cb.fromRGB(140,110,0)
citro = cb.fromRGB(110,128,0)
green = cb.fromRGB(0,128,0)
petrol = cb.fromRGB(0,110,110)
blue = cb.fromRGB(0,0,128)
purple = cb.fromRGB(110,0,110)
red = cb.fromRGB(128,0,0)
orange = cb.fromRGB(134,55,0)

#--------------------------------------------------------------------------------

#Pixel
#setpix(nx,ny,nz,cl)
#cbs.setpix(0, 0, 0, green)

#Nummer
#cbs.number(num,z-deepness,cl)
#cbs.number(1, 1, green)

#Linie, Orientierung ori (0,1,2 entlang x,y,z-Achse), 2D-Koordinaten ko1,ko2 (0..(side-1), Beginn st, Laenge le, Farbe cl)  
#line(ori,ko1,ko2,st,le,cl)
#cbs.line(2, 1, 1, 1, 2, white)

#Quadratflaeche, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
#slice(ori,lev,st1,st2,le,cl)
#cbs.slice(0, 0, 1, 2, 2, white)

#Quadrat, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
#square(ori,lev,st1,st2,le,cl)
#cbs.square(1, 0, 1, 2, 3, white)

#Wuerfel, ausgefuellt, Offset x,y,z, Kantenlaenge le, Farbe cl
#fcube(ox, oy, oz, le, cl)
#cbs.fcube(0, 0, 0, side, white)

#--------------------------------------------------------------------------------

while True:

 # rainbow

 cb.rainbow()
 cb.show()

 time.sleep(3)

 # white slices

 for i in range(side):
   cbs.slice(2,i,0,0,side,white)
   cb.show()
   time.sleep(0.08)
   cbs.slice(2,i,0,0,side,black)
   cb.show()

 time.sleep(0.2)

 for i in range(side):
   cbs.slice(2,i,0,0,side,grey1)
   cb.show()
   time.sleep(0.04)
   cb.show()

 time.sleep(0.5)

 for i in range(side):
   cbs.slice(2,i,0,0,side,grey2)
   cb.show()
   time.sleep(0.02)
   cb.show()

 time.sleep(0.8)

 # green squares

 for i in range(side):
   cbs.square(0,i,0,0,side,green)
   cb.show()
   time.sleep(0.25)

 time.sleep(1)
 cb.clear()

 # numbers

 i = 0
 for i in range(10):

   cl = white
   if (i > 0): cl = yellow
   if (i > 1): cl = citro
   if (i > 2): cl = green
   if (i > 3): cl = petrol
   if (i > 4): cl = blue
   if (i > 5): cl = purple
   if (i > 6): cl = red
   if (i > 7): cl = orange
   if (i > 8): cl = grey1
   d = 0
   for d in range(side):

      cbs.number(i, d, cl)
      cb.show()
      time.sleep(0.02)
      if (d == 3): time.sleep(0.05)
      if (d == 2): time.sleep(0.1)
      if (d == 1): time.sleep(0.2)
      if (d == 0): time.sleep(0.5)
      cb.clear()

 time.sleep(1)

 # blue squares

 for i in range(side):
   cbs.square(0,(4-i),0,0,side,cb.fromRGB((i*20),0,128))
   cb.show()
   time.sleep(0.15)

 time.sleep(1.5)

 # red lines

 for i in range(side):
   cbs.line(1,i,0,0,5,red)
   cbs.line(1,0,i,0,5,red)
   cbs.line(1,(4-i),4,0,5,red)
   cbs.line(1,4,(4-i),0,5,red)
   cb.show()
   time.sleep(0.25)

 for i in range(side-1):
   cbs.line(1,(i+1),1,0,5,red)
   cbs.line(1,1,(i+1),0,5,red)
   cbs.line(1,(3-i),3,0,5,red)
   cbs.line(1,3,(3-i),0,5,red)
   cb.show()
   time.sleep(0.15)

 cbs.line(1,2,2,0,5,red)
 cb.show()

 time.sleep(1)
 cb.clear()

 # spinner

 for sc in range(12):
   iz = 0
   ix = 0
   for ix in range(side):
      cbs.setpix(ix,0,iz,petrol)
      cbs.setpix(ix,(side-1),iz,petrol)
      cb.show()
      time.sleep(0.01)
      cb.clear()
   iz = 0
   ix = (side-1)
   for iz in range(side):
      cbs.setpix(ix,0,iz,petrol)
      cbs.setpix(ix,(side-1),iz,petrol)
      cb.show()
      time.sleep(0.01)
      cb.clear()
   iz = (side-1)
   ix = 0
   for ix in range(side):
      cbs.setpix(side-1-ix,0,iz,petrol)
      cbs.setpix(side-1-ix,(side-1),iz,petrol)
      cb.show()
      time.sleep(0.01)
      cb.clear()
   ix = 0
   iz = 0
   for iz in range(side):
      cbs.setpix(ix,0,side-1-iz,petrol)
      cbs.setpix(ix,(side-1),side-1-iz,petrol)
      cb.show()
      time.sleep(0.01)
      cb.clear()

 # white slices

 for i in range(side):
   cbs.slice(2,i,0,0,side,white)
   cb.show()
   time.sleep(0.08)
   cbs.slice(2,i,0,0,side,black)
   cb.show()

 time.sleep(0.2)

 for i in range(side):
   cbs.slice(2,i,0,0,side,grey1)
   cb.show()
   time.sleep(0.05)
   cb.show()

 time.sleep(0.5)

 for i in range(side):
   cbs.slice(2,i,0,0,side,grey2)
   cb.show()
   time.sleep(0.02)
   cb.show()

 time.sleep(3)
 cb.clear()

 # yellow cube

 cbs.line(0,0,0,0,5,yellow)
 cbs.line(0,4,0,0,5,yellow)

 cbs.line(0,0,4,0,5,yellow)
 cbs.line(0,4,4,0,5,yellow)

 cbs.line(1,0,0,0,5,yellow)
 cbs.line(1,4,0,0,5,yellow)

 cbs.line(1,0,4,0,5,yellow)
 cbs.line(1,4,4,0,5,yellow)

 cbs.line(2,0,0,0,5,yellow)
 cbs.line(2,4,0,0,5,yellow)

 cbs.line(2,0,4,0,5,yellow)
 cbs.line(2,4,4,0,5,yellow)
 cb.show()

 time.sleep(3)

 # purple rain

 cbs.purplerain()

 # rainbow

 cb.rainbow()
 cb.show()
 time.sleep(3)
 cb.clear()

cb.cleanup()

#--------------------------------------------------------------------------------
