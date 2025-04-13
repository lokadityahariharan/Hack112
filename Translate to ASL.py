from cmu_graphics import *
import time

image_folder = '/Users/veydpatil/Desktop/112 TP/ASL handlib/'



def onAppStart(app):
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
    app.stepsPerSecond = 1000
    app.currIndex = False

    app.text = input("Enter text to translate into ASL: ")
    app.drawing = False



def onMousePress(app,mouseX,mouseY):
    if app.currIndex >=len(app.text) - 1:
        app.currIndex = 0
    else:
        app.currIndex += 1

    

def translateToASL(app):
    asl_images = []
    for char in app.text.upper():
        if char in app.imageDict:
            asl_images.append(app.imageDict[char])
    return asl_images

def showImages(app, imageList):
    drawImage(image_folder + imageList[app.currIndex], app.width/2, 
              app.height/2, width=100, height=100,align='center')
        


def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='white')

    images = translateToASL(app)
    showImages(app, images)

def main():
    pass

runApp()
cmu_graphics.run()