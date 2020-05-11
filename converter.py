# convert.py 
# Tyler 
# convert celcius to farenheit 

from graphics import *

def main():
    #create window obj
    win = GraphWin("Converter",400,300)
    #create text objects
    celsiusTempString =  "Celsius Temperature:   "
    farenheitTempString = "Farenheit Temperature:"
    #text box
    Text(Point(150,50), celsiusTempString).draw(win)
    Text(Point(150,250),farenheitTempString).draw(win)

    #create center box
    Rectangle(Point(125,100),Point(275,200)).draw(win)

    # create button text
    buttonText= Text(Point(200,150),"Convert It")
    buttonText.draw(win)

    #input output fields
    inputCelsiusField= Entry(Point(300,50),5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)

    outputFarenheitField= Text(Point(300,250),"")
    outputFarenheitField.draw(win)
    win.getMouse()

    celsiusTemperature = float(inputCelsiusField.getText())
    farenheit = 9.0/5.0 * celsiusTemperature + 32

    #display
    outputFarenheitField.setText(round(farenheit, 2))
    buttonText.setText("Quit")

    win.getMouse()

main()