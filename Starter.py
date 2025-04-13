from cmu_graphics import *

def onAppStart(app):
    app.color = 'gray'
    app.buttonOneX = app.width/2    
    app.buttonTwoX = app.width/2
    app.buttonOneY = 125
    app.buttonTwoY = 275
    app.insideBoxOne = False
    app.insideBoxTwo = False
    app.translateToASL = False
    app.translateFromASL = False
    app.text = ''
    app.stepsPerSecond = 8
    app.stepCount = 0
    app.keys = set()
    app.backspaceHeld = False

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
    app.insideBoxOne = (app.buttonOneX - 100 < mouseX < app.buttonOneX + 100 and
                      app.buttonOneY - 50 < mouseY < app.buttonOneY + 50)
    app.insideBoxTwo = (app.buttonTwoX - 100 < mouseX < app.buttonTwoX + 100 and
                      app.buttonTwoY - 50 < mouseY < app.buttonTwoY + 50)
def onStep(app):
    app.stepCount += 1
    if app.backspaceHeld and app.text != '':
        app.text = app.text[:-1]

def onMousePress(app, mouseX, mouseY):
    if (app.buttonOneX - 100 < mouseX < app.buttonOneX + 100 and
        app.buttonOneY - 50 < mouseY < app.buttonOneY + 50):
        app.translateToASL = True
    elif (app.buttonTwoX - 100 < mouseX < app.buttonTwoX + 100 and
          app.buttonTwoY - 50 < mouseY < app.buttonTwoY + 50):
        app.translateFromASL = True
    elif (32.5 < mouseX < 102.5 and 340 < mouseY < 380):
        app.translateToASL = False
        app.translateFromASL = False
    
def drawFirstScreen(app):
    if not app.translateToASL and not app.translateFromASL:
        colorOne = 'black' if app.insideBoxOne else 'gray'
        colorTwo = 'black' if app.insideBoxTwo else 'gray'
        drawLabel('ASL Translator', app.width/2, 30, size = 30, bold = True)
        drawRect(app.buttonOneX, app.buttonOneY, 200, 100, fill = colorOne,
                border='black',align='center', opacity = 50)
        drawRect(app.buttonTwoX, app.buttonTwoY, 200, 100, fill = colorTwo,
                border='black',align='center', opacity = 50)
        drawLabel('Translate to ASL', app.buttonOneX, app.buttonOneY, bold = True, size = 20)
        drawLabel('Translate from ASL', app.buttonTwoX, app.buttonTwoY, bold = True, size = 20)

def drawTranslateToASL(app):
    if app.translateToASL:
        lineX = 57 + 9.3 * len(app.text)
        drawLabel('Translate to ASL', app.width/2, 30, size = 30, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
        drawRect(200, 100, 300, 50, fill = None, border = 'black', align = 'center')
        drawLabel(app.text, 56, 100, size = 20, align = 'left')
        if app.stepCount % 8 == 0:
            drawLine(lineX, 80, lineX, 120)

def redrawAll(app):
    drawFirstScreen(app)
    drawTranslateToASL(app)
    if app.translateFromASL:
        drawLabel('Translate from ASL', app.width/2, 30, size = 30, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)

def main():
    runApp()

main()