import tkinter

# this is View class that contains all controls
class MyFrame(tkinter.Frame):

    # constructor of View takes controller object as parameter
    def __init__ (self, controller):
        tkinter.Frame.__init__ (self)
        self.pack()
        self.controller = controller  # saves a reference to the controller so that we can call methods
        # on the controller object when the user generates  events

        self.txtFahrenheit = tkinter.Entry()
        self.txtFahrenheit.insert(0, "Fahrenheit temp.")
        self.txtFahrenheit.pack({"side": "left"})
        
        self.btnFahrenheitToCelsius = tkinter.Button(self)
        self.btnFahrenheitToCelsius["text"] = "Fahrenheit To Celsius"
        self.btnFahrenheitToCelsius["command"] = self.controller.btnFahrenheitToCelsiusClicked
        self.btnFahrenheitToCelsius.pack({"side": "left"})

        self.txtCelsius = tkinter.Entry()
        self.txtCelsius.insert(0, "Celsius temp.")
        self.txtCelsius.pack({"side": "left"})

        self.btnCelsiusToFahrenheit = tkinter.Button(self)
        self.btnCelsiusToFahrenheit["text"] = "Celsius To Fahrenheit"
        self.btnCelsiusToFahrenheit["command"] = self.controller.btnCelsiusToFarenheightClicked
        self.btnCelsiusToFahrenheit.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "left"})
