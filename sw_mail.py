#!/usr/bin/python

# displaying mail messages...
# sw_mail.py

# author        : Swen Hopfe
# created       : 22-01-10
# last modified : 22-02-18

#--------------------------------------------------------------------------------

import cubebit as cb
import swc as cbs
import time
import random
import imaplib
import email

demo = True

gcnt = 0
mcnt = 0

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

# Empfangsteil

if not demo:

    USER = "xxxx"
    PASS = "xxxx"
    SERVER = "xxx.xxx.xx"

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(USER,PASS)

    mcnt = 0

    # Posteingang auswaehlen
    type, data = mail.select('INBOX')

    # nach bestimmtem Substring im Betreff (leer "" alles) filtern und in Liste ablegen

    type, [mids] = mail.uid('search',None,'(UNSEEN SUBJECT "")')

    if mids:

        # fuer alle ermittelten Mail-IDs
        for id in mids.split():
            mcnt = mcnt + 1
        print("Anzahl Nachrichten:")
        print(mcnt)

    else:
        print("Keine neuen Nachrichten gefunden.")

    mail.close()
    mail.logout()

else:

    mcnt = 2

    print("Anzahl Nachrichten (Demo): 2")

# Anzeigeteil --------------------

if mcnt > 9:
    str = str(mcnt)
    i1 = int(str[0])
    i2 = int(str[1])

if mcnt > 0:

  print("Nachrichten eingegangen, starte Anzeige...")

  while gcnt < 5:

    if mcnt < 10:

        i = mcnt

        d = 0
        for d in range(side-1):
            cbs.number(i, d+1 , petrol)
            cb.show()
            time.sleep(0.05)
            if (d == 2): time.sleep(0.1)
            if (d == 1): time.sleep(0.2)
            if (d == 0): time.sleep(0.5)
            cb.clear()

        cbs.number(i, 1, petrol)
        cb.show()

    else:
        if mcnt < 100:

            d = 0
            for d in range(side-1):
                cbs.number(i2, d+1 , petrol)
                cb.show()
                time.sleep(0.05)
                if (d == 2): time.sleep(0.1)
                if (d == 1): time.sleep(0.2)
                if (d == 0): time.sleep(0.5)
                cb.clear()

            cbs.number(i1, 3, white)
            cbs.number(i2, 1, petrol)
            cb.show()

    gcnt = gcnt + 1
    time.sleep(5)

  zcnt = 0
  while zcnt < 30:
    zcnt = zcnt + 1
    time.sleep(1)
  #cb.clear()

cb.cleanup()

#--------------------------------------------------------------------------------




