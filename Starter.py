from cmu_graphics import *
import cv2

def onAppStart(app):
    app.color = 'gray'   
    app.insideBoxOne = False
    app.insideBoxTwo = False
    app.translateToASL = False
    app.translateFromASL = False
    app.text = ''
    app.stepsPerSecond = 8
    app.stepCount = 0
    app.keys = set()
    app.backspaceHeld = False
    app.showDash = False

def onKeyPress(app, key):
    if app.translateToASL and (key.isalpha() or key.isspace()):
        if key == 'space':
            app.text += ' '
        elif key == 'backspace':
            app.backspaceHeld = True
        else:
            app.text += key

def onKeyRelease(app, key):
    if key == 'backspace':
        app.backspaceHeld = False

def onMouseMove(app, mouseX, mouseY):
    app.insideBoxOne = (app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
                      app.height*0.3125 - app.height/8 < mouseY < app.height*0.3125 + app.height/8)
    app.insideBoxTwo = (app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
                      app.height*0.6875 - app.height/8 < mouseY < app.height*0.6875 + app.height/8)
def onStep(app):
    app.stepCount += 1
    if app.backspaceHeld and app.text != '':
        app.text = app.text[:-1]

def onMousePress(app, mouseX, mouseY):
    if (not app.translateFromASL and app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
        app.height*0.3125 - app.height/8 < mouseY < app.height*0.3125 + app.height/8):
        app.translateToASL = True
    elif (not app.translateToASL and app.width/2 - app.width/4 < mouseX < app.width/2 + app.width/4 and
          app.height*0.6875 - app.height/8 < mouseY < app.height*0.6875 + app.height/8):
        app.translateFromASL = True
    elif (32.5 < mouseX < 102.5 and app.height-60 < mouseY < app.height-20):
        app.translateToASL = False
        app.translateFromASL = False
    
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
        lineX = app.width*.1425 + 9.3 * len(app.text)
        drawLabel('Translate to ASL', app.width/2, app.width*0.07, size = app.width*0.075, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
        drawRect(app.width/2, app.height/4, app.width*0.75, app.height/8, fill = None, border = 'black', align = 'center')
        drawLabel(app.text, app.width*0.14, app.height/4, size = app.width*0.05, align = 'left')
        if app.stepCount % 8 == 0:
            drawLine(lineX, app.height*0.2, lineX, app.height*0.3)

def drawTranslateFromASL(app):
    if app.translateFromASL:
        drawLabel('Translate from ASL', app.width/2, app.width*0.07, size = app.width*0.075, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
        

def redrawAll(app):
    drawFirstScreen(app)
    drawTranslateToASL(app)
    drawTranslateFromASL(app)

def main():
    runApp()

if __name__ == "__main__":
    main()