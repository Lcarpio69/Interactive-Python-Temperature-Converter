import tkinter
import myView  # the VIEW
import myModel  # the MODEL

# this is controller class that binds the View and Model classes
class Controller:
    """
    The Controller for an app that follows the Model/View/Controller architecture.
    When the user presses a Button on the View, this Controller calls the appropriate
    methods in the Model. The Controller handles all communication between the Model
    and the View.
    """

    def __init__(self):
        """
        This starts the Tk framework up, instantiates the Model (a Converter object),
        instantiates the View (a MyFrame object), and starts the event loop that waits
        for the user to press a Button on the View.
        """
        root = tkinter.Tk()
        self.model = myModel.Converter()
        self.view = myView.MyFrame(self)
        self.view.mainloop()
        root.destroy()

    def btnFahrenheitToCelsiusClicked(self):
        """
        Python calls this method when the user presses the Fahrenheit To Celsius button in the View.
        """
        self.view.txtCelsius.delete(0, 'end')
        self.view.txtCelsius.insert(0, self.model.fahrenheitToCelsius(float(self.view.txtFahrenheit.get())))

    def btnCelsiusToFarenheightClicked(self):
        """
        Python calls this method when the user presses the Celsius To Fahrenheit button in the View.
        """
        self.view.txtFahrenheit.delete(0, 'end')
        self.view.txtFahrenheit.insert(0, self.model.celsiusTofahrenheit(float(self.view.txtCelsius.get())))

if __name__ == "__main__":
    c = Controller()
