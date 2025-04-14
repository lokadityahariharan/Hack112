from cmu_graphics import *
import cv2
import os 
import mediapipe as mp
import numpy as np
import joblib
import time
import math as math

from PIL import Image as PILImage
from ASLto import translateFromASL
from TranslatetoASL import translateASL


image_folder = 'ASL handlib/'

def onAppStart(app):
    app.color = 'gray'   
    app.insideBoxOne = False
    app.insideBoxTwo = False
    app.translateToASL = False
    app.translateFromASL = False
    app.text = ''
    app.stepsPerSecond = 80
    app.stepCount = 0
    app.keys = set()
    app.dashOpacity = 50
    app.dashDo = 2

    #Camera and ASL model
    app.cap = cv2.VideoCapture(0)
    app.model = joblib.load('asl_knn_model.pkl')
    app.hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
    app.mp_draw = mp.solutions.drawing_utils
    app.prediction = ''
    app.videoFrame = None


    #Translate to ASL Variables 
    app.imageDict = {
        'A': 'A.png',
        'B': 'B.png',
        'C': 'C.png',
        'D': 'D.png',
        'E': 'E.png',
        'F': 'F.png',
        'G': 'G.png',
        'H': 'H.png',
        'I': 'I.png',
        'J': 'J.png',
        'K': 'K.png',
        'L': 'L.png',
        'M': 'M.png',
        'N': 'N.png',
        'O': 'O.png',
        'P': 'P.png',
        'Q': 'Q.png',
        'R': 'R.png',
        'S': 'S.png',
        'T': 'T.png',
        'U': 'U.png',
        'V': 'V.png',
        'W': 'W.png',
        'X': 'X.png',
        'Y': 'Y.png',
        'Z': 'Z.png',
    }
    app.startASL = False



def onKeyPress(app, key):
    if app.translateToASL and (key.isalpha() or key.isspace()) and key != 'enter':
        if key == 'space':
            app.text += ' '
        elif key == 'backspace':
            app.text = app.text[:-1]
        else:
            app.text += key
    elif app.translateToASL and key == 'enter':
        app.startASL = True




def onMouseMove(app, mouseX, mouseY):
    app.insideBoxOne = (app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
                      app.height*0.3125 - app.height/8 < mouseY < app.height*0.3125 + app.height/8)
    app.insideBoxTwo = (app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
                      app.height*0.6875 - app.height/8 < mouseY < app.height*0.6875 + app.height/8)
    

def onStep(app):
    app.stepCount += 1
    if app.dashOpacity <= 8:
        app.dashDo = -1 * app.dashDo
    elif app.dashOpacity >= 80:
        app.dashDo = -1 * app.dashDo
    app.dashOpacity += app.dashDo

    if app.translateFromASL:
        success, img = app.cap.read()
        if success:
            app.prediction, transImg = translateFromASL(img, app.model, app.hands, app.mp_draw)
            
            img_rgb = cv2.cvtColor(transImg, cv2.COLOR_BGR2RGB)
            pil_image = PILImage.fromarray(img_rgb)
            temp_path = "temp_image.png"
            pil_image.save(temp_path)
            app.videoFrame = temp_path

            

def onMousePress(app, mouseX, mouseY):
    if ((app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
        app.height*0.3125 - app.height/8 < mouseY < app.height*0.3125 + app.height/8) 
        and app.translateFromASL == False):
        app.translateToASL = True
    elif (app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
          app.height*0.6875 - app.height/8 < mouseY < app.height*0.6875 + app.height/8 
          and app.translateToASL == False):
        app.translateFromASL = True
        #translateFromASL()

    elif (32.5 < mouseX < 102.5 and app.height-60 < mouseY < app.height-20):
        app.translateToASL = False
        app.translateFromASL = False
        app.text = ''
    


def drawFirstScreen(app):
    if not app.translateToASL and not app.translateFromASL:
        colorOne = 'black' if app.insideBoxOne else 'gray'
        colorTwo = 'black' if app.insideBoxTwo else 'gray'
        drawLabel('ASL Translator', app.width/2, app.width*0.07, size = app.width*0.075, bold = True)
        drawRect(app.width/2, app.height*0.3125, app.width/2, app.height/4, fill = colorOne,
                border='black',align='center', opacity = 50)
        drawRect(app.width/2, app.height*0.6875, app.width/2, app.height/4, fill = colorTwo,
                border='black',align='center', opacity = 50)
        drawLabel('Translate to ASL', app.width/2, app.height*0.3125, bold = True, size = app.width*0.05)
        drawLabel('Translate from ASL', app.width/2, app.height*0.6875, bold = True, size = app.width*0.05)



def drawTranslateToASL(app):
    if app.translateToASL:
        lineX = app.width*.1425 + 9.5 * len(app.text)
        drawLabel('Translate to ASL', app.width/2, app.width*0.07, size = app.width*0.075, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
        drawRect(app.width/2, app.height/4, app.width*0.75, app.height/8, fill = None, border = 'black', align = 'center')
        drawLabel(app.text, app.width*0.14, app.height/4, size = app.width*0.05, align = 'left')
        #if app.stepCount % 80 == 0:
        drawLine(lineX, app.height*0.2, lineX, app.height*0.3,opacity= app.dashOpacity)
        #translateToASL(app, app.text)



def drawTranslateFromASL(app):
    if app.translateFromASL:
        drawLabel('Translate from ASL', app.width/2, app.width*0.07, size = app.width*0.075, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
        drawLabel(f"Prediction: {app.prediction}", app.width/2, app.height/4, size = app.width*0.05)

        if app.videoFrame:
            drawImage(app.videoFrame,app.width/2,app.height/2, width = 400, height = 300, align = 'center')



def redrawAll(app):
    drawFirstScreen(app)
    drawTranslateToASL(app)
    drawTranslateFromASL(app)

def main():
    runApp()

main()