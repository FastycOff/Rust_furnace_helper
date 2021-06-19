from mss import mss
import cv2
import numpy
import time
from PIL import Image
import pytesseract
import ctypes
import os
import keyboard
pytesseract.pytesseract.tesseract_cmd = r"C:\..."
X_Furnace = 1#(classic Server (x1 furnaces))
    
def pop(msg):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, msg, 'Window title', 0x40000)
    
def scan_resources(): 
    with mss() as sct:
        mon_name = {"top": 105, "left": 660, "width":170, "height": 35}
        mon_cout = {"top": 515, "left": 1195, "width":50, "height": 15}
        name = numpy.asarray(sct.grab(mon_name))
        count= numpy.asarray(sct.grab(mon_cout))
    
        #cv2.imshow("hello_world", name)   #Debug
        #cv2.imshow("hello", count)        #Debug
        
    name_text = pytesseract.image_to_string(name, lang="eng", config="--dpi 600 --oem 1 --psm 13") # ore name
    int_count = pytesseract.image_to_string(count, lang="eng", config="--dpi 600 --oem 1 --psm 9") # ore count 
    ore = ""
    count=""
    for i in range(0,4):
        ore += name_text[i]
        
    for i in range(len(int_count)):
        if int_count[i].isdigit() == True:
            count += int_count[i]
        
    #print(ore)     #Debug
    #print(count)   #Debug
            
    if ore == "META":
        try:
            pop("Wood: " + str(round(int(count)/0.6/X_Furnace)) + " Metal: " + str(count))
        except:
            pop("Attempt failed")
            
    elif ore == "SULF":
        try:
            pop("Wood: " + str(round(int(count)/1.2/X_Furnace)) + " Sulfur: " + str(count))
        except:
            pop("Attempt failed")
            
    elif ore == "HIGH":
        try:
            pop("Wood: " + str(round(int(count)/0.3/X_Furnace)) + " HQM: " + str(count))
            
        except:
            pop("Attempt failed")
        
        
while True:
    if keyboard.is_pressed("insert"):
        scan_resources()
