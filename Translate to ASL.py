from cmu_graphics import *

image_folder = #Insert the path to your image folder here

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
    app.textToTranslate = input("Enter text to translate into ASL: ")
    

def translateToASL(app):
    text = input("Enter text to translate into ASL: ")
    asl_images = []
    for char in text.upper():
        if char in app.imageDict:
            asl_images.append(app.imageDict[char])
    return asl_images

def showImages(app, images):
    for image in images:
        img = Image(app.imageDict[image], x=app.width/2, y=app.height/2, width=50, height=50)
        img.draw()
        delay(1000)

cmu_graphics.run()