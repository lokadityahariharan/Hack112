from cmu_graphics import *

def onAppStart(app):
    app.color = 'white'

def onMousePress(app, mouseX, mouseY):
    if app.width/2 - 75 < mouseX < app.width/2 + 75 and app.height/2 - 25 < mouseY < app.height/2 + 25:
        app.translate = True
    else:
        app.translate = False
    pass

def redrawAll(app):
    drawRect(app.width/2, app.height/2,150,50, fill = app.color,
             border='black',align='center')
    drawLabel('Translate to ASL', app.width/2, app.height/2, font='A', bold = True)

def main():
    runApp()

main()