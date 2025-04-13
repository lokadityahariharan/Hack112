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

def onMouseMove(app, mouseX, mouseY):
    app.insideBoxOne = (app.buttonOneX - 100 < mouseX < app.buttonOneX + 100 and
                      app.buttonOneY - 50 < mouseY < app.buttonOneY + 50)
    app.insideBoxTwo = (app.buttonTwoX - 100 < mouseX < app.buttonTwoX + 100 and
                      app.buttonTwoY - 50 < mouseY < app.buttonTwoY + 50)

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


def redrawAll(app):
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
    elif app.translateToASL:
        drawLabel('Translate to ASL', app.width/2, 30, size = 30, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)
    elif app.translateFromASL:
        drawLabel('Translate from ASL', app.width/2, 30, size = 30, bold = True)
        drawRect(70, app.height - 40, 75, 40, fill = 'red', opacity = 75, align = 'center', border = 'black')
        drawLabel('Back', 70, app.height - 40, size = 20)

def main():
    runApp()

main()