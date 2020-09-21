

# this class has two methods that converts temperatures
# this is the model class
class Converter:
    # function that take temperature in fahrenheit and convert it to celsius and return
    # takes parameter in fahrenheit
    # returns temperature in celsius
    def fahrenheitToCelsius(self, Tf):
        return (5/9)*(Tf-32)

    # function that take temperature in celsius and convert it to fahrenheit and return
    # takes parameter in celsius
    # returns temperature in fahrenheit
    def celsiusTofahrenheit(self, Tc):
        return ((9/5)*Tc)+32
