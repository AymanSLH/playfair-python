from appJar import gui
from index import *
app = gui()

app.addLabel("Playfiar" , "Playfair Algorithm")

def press(button):
    if button=="Cancel" :
        app.stop()
    else:
        myText = app.getEntry('Text')
        myKey = app.getEntry("Key")
        (encode, decode) = playfair(myKey)
        enc = encode(myText)
        app.infoBox("Result" ,"The result is : "+ enc)

app.addLabelEntry("Text")
app.addLabelEntry("Key")
app.addButtons(["Submit", "Cancel"], press)
app.go()