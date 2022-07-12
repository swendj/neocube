#!/usr/bin/python

# This is our "swc" class working together with "sw_cube.py" based on the python port "cubebit.py".
# Just use "sw_cube.py" to see what's possible.

# author        : Swen Hopfe
# created       : 22-01-10
# last modified : 22-02-18

#--------------------------------------------------------------------------------

import cubebit as cb
import time
import random

side = 5

def init (lside=3):
        global side
        side = lside

#--------------------------------------------------------------------------------
#
#      # # #  # #
#     #       # #
#    # # # # #  #
#    #       #  #
#  y #       # # z
#    #       ##
#    # # # # #
#        x
#
#--------------------------------------------------------------------------------

# Linie, Orientierung ori (0,1,2 entlang x,y,z-Achse), 2D-Koordinaten ko1,ko2 (0..(side-1), Beginn st, Laenge le, Farbe cl)  

def line(ori,ko1,ko2,st,le,cl):

#    # # # # #
#    ko1=y ko2=z   Linie in x-Richtung

  if ori == 0:
     for x in range(le):
        cb.setPixel(cb.map((side-x-st-1), ko2, ko1),cl)

#    #
#    #
#    #  ko2=z      Linie in y-Richtung
# ko1=x

  elif ori == 1:
     for z in range(le):
         cb.setPixel(cb.map((side-ko1-1), ko2, (z+st)),cl)

#      #
#     #
#    #  ko2=y      Linie in z-Richtung
# ko1=x

  elif ori == 2:
     for y in range(le):
         cb.setPixel(cb.map((side-ko1-1), (y+st), ko2),cl)

#-----------------------------------------------------------

# Quadratflaeche, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  

def slice(ori,lev,st1,st2,le,cl):


#    # # # # #  lev
#    # # # # #

  if ori == 0:
     for y in range(le):
       for x in range(le):
         cb.setPixel(cb.map((side-x-st1-1), (y+st2), lev),cl)

#   # # st2
#   # # st1
#   # #
#   lev

  elif ori == 1:
     for z in range(le):
       for y in range(le):
         cb.setPixel(cb.map((side-lev-1), (y+st2), (z+st1)),cl)

#     # # lev
#   # #
#   # # st2
#   st1

  elif ori == 2:
     for z in range(le):
       for x in range(le):
         cb.setPixel(cb.map((side-x-st1-1), lev, (z+st2)),cl)

#-----------------------------------------------------------

# Quadrat, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  

def square(ori,lev,st1,st2,le,cl):


#    # # # # #  lev
#    # # # # #

  if ori == 0:
     for x in 0,(le-1):
       for y in range(le-2):
         cb.setPixel(cb.map((side-x-st1-1), (y+1+st2), lev),cl)
     for y in 0,(le-1):
       for x in range(le):
         cb.setPixel(cb.map((side-x-st1-1), (y+st2), lev),cl)

#   # # st2
#   # # st1
#   # #
#   lev

  elif ori == 1:
     for y in 0,(le-1):
       for z in range(le-2):
         cb.setPixel(cb.map((side-lev-1), (y+st2), (z+st1+1)),cl)
     for z in 0,(le-1):
       for y in range(le):
         cb.setPixel(cb.map((side-lev-1), (y+st2), (z+st1)),cl)

#     # # lev
#   # #
#   # # st2
#   st1

  elif ori == 2:
     for x in 0,(le-1):
       for z in range(le-2):
         cb.setPixel(cb.map((side-x-st1-1), lev, (z+1+st2)),cl)
     for z in 0,(le-1):
       for x in range(le):
         cb.setPixel(cb.map((side-x-st1-1), lev, (z+st2)),cl)

#-----------------------------------------------------------

# Wuerfel, ausgefuellt, Offset x,y,z, Kantenlaenge le, Farbe cl

def fcube(ox, oy, oz, le, cl):

   for z in range(le):
      for y in range(le):
         for x in range(le):
            cb.setPixel(cb.map((side-x-ox-1), (z+oz), (y+oy)),cl)

#-----------------------------------------------------------

# setpix(x, y, z, cl)
# cl - color
# (x=0, y=0, z=0) is bottom, left, front
#
#   4 #       #
#     #     # 4
#     #   #
#     # #
#   0 # # # # #
#   0 0       4

def setpix(nx, ny, nz, cl):

   cb.setPixel(cb.map((side-1-nx), (nz), (ny)),cl)

#-----------------------------------------------------------

# number "0"
# dp - Deepness (move in z-direction)

def n_0(dp, cl):

   line(1, 1, dp, 0, 5, cl)
   line(1, 3, dp, 0, 5, cl)
   setpix(2, 0, dp, cl)
   setpix(2, 4, dp, cl)

#-----------------------------------------------------------

# number "1"

def n_1(dp, cl):

   line(1, 2, dp, 0, 5, cl)
   setpix(1, 3, dp, cl)

#-----------------------------------------------------------

# number "2"

def n_2(dp, cl):

   line(0, 0, dp, 1, 3, cl)
   line(0, 2, dp, 1, 3, cl)
   line(0, 4, dp, 1, 3, cl)
   setpix(1, 1, dp, cl)
   setpix(3, 3, dp, cl)

#-----------------------------------------------------------

# number "3"

def n_3(dp, cl):

   line(0, 0, dp, 1, 3, cl)
   line(0, 2, dp, 2, 2, cl)
   line(0, 4, dp, 1, 3, cl)
   setpix(3, 1, dp, cl)
   setpix(3, 3, dp, cl)

#-----------------------------------------------------------

# number "4"

def n_4(dp, cl):

   line(1, 1, dp, 2, 3, cl)
   line(1, 3, dp, 0, 5, cl)
   setpix(2, 2, dp, cl)

#-----------------------------------------------------------

# number "5"

def n_5(dp, cl):

   line(0, 0, dp, 1, 3, cl)
   line(0, 2, dp, 1, 3, cl)
   line(0, 4, dp, 1, 3, cl)
   setpix(1, 3, dp, cl)
   setpix(3, 1, dp, cl)

#-----------------------------------------------------------

# number "6"

def n_6(dp, cl):

   line(0, 0, dp, 1, 3, cl)
   line(0, 2, dp, 1, 3, cl)
   line(0, 4, dp, 1, 2, cl)
   setpix(1, 1, dp, cl)
   setpix(1, 3, dp, cl)
   setpix(3, 1, dp, cl)

#-----------------------------------------------------------

# number "7"

def n_7(dp, cl):

   line(0, 4, dp, 1, 3, cl)
   line(1, 1, dp, 0, 2, cl)
   setpix(2, 2, dp, cl)
   setpix(3, 3, dp, cl)

#-----------------------------------------------------------

# number "8"

def n_8(dp, cl):

   line(1, 1, dp, 0, 5, cl)
   line(1, 3, dp, 0, 5, cl)
   setpix(2, 0, dp, cl)
   setpix(2, 2, dp, cl)
   setpix(2, 4, dp, cl)

#-----------------------------------------------------------

# number "9"

def n_9(dp, cl):

   line(1, 1, dp, 2, 3, cl)
   line(1, 3, dp, 0, 5, cl)
   setpix(2, 0, dp, cl)
   setpix(2, 2, dp, cl)
   setpix(2, 4, dp, cl)

#-----------------------------------------------------------

# number

def number(num, dp, cl):

  if num == 0: n_0(dp, cl)
  if num == 1: n_1(dp, cl)
  if num == 2: n_2(dp, cl)
  if num == 3: n_3(dp, cl)
  if num == 4: n_4(dp, cl)
  if num == 5: n_5(dp, cl)
  if num == 6: n_6(dp, cl)
  if num == 7: n_7(dp, cl)
  if num == 8: n_8(dp, cl)
  if num == 9: n_9(dp, cl)

#-----------------------------------------------------------

# from "purplerain", out of original examples for the "cube:bit" library

side2 = side*side
rain = cb.fromRGB(128,0,128)
white = cb.fromRGB(128,128,128)
cloud = [None]*side2

def purplerain():

        cb.clear()
        cb.setPlane(side-1, 2, rain)
        cb.show()
        time.sleep(1)
        cb.setColor(white)
        cb.show()
        time.sleep(0.05)
        cb.clear()
        cb.setPlane(side-1,2,rain)
        cb.show()
        for i in range(side2):
            cloud[i] = 0
        for k in range(side2):
            x = random.randint(0,side-1)
            y = random.randint(0,side-1)
            while (cloud[x+y*side] != 0):
                x = random.randint(0,side-1)
                y = random.randint(0,side-1)
            cloud[x + y*side] = 1
            for i in range(side-1):
                cb.setPixel(cb.map(x,y,side-1-i), 0)
                cb.setPixel(cb.map(x,y,side-2-i), rain)
                cb.show()
                time.sleep(0.2)
        time.sleep(1)
        for y in range(side-1):
            for x in range(side):
                cb.setPixel(cb.map(x, side-y-1, 0), 0)
                cb.setPixel(cb.map(x, 0, y+1), rain)
            cb.show()
            time.sleep(0.2)
        for y in range(side-1):
            for x in range(side):
                cb.setPixel(cb.map(x, 0, y), 0)
                cb.setPixel(cb.map(x, y+1, side-1), rain)
            cb.show()
            time.sleep(0.2)
        time.sleep(1)

#--------------------------------------------------------------------------------
