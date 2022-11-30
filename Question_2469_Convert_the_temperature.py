class Solution:
    def convertTemperature(self, celsius: float):
        kelvin = celsius + 273.15
        Fah = celsius*1.8 + 32
        return [kelvin, Fah]