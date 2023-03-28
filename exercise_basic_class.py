'''Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class'''

class MedPlus:
    def __init__(self, name: str, batch_number: int, price: float):
        if type (name) is not str:
            raise TypeError("Name must be a string")
        if not isinstance(batch_number, int):
            raise TypeError("Batch number must be an integer")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if batch_number <= 0:
            raise ValueError("Batch number must be greater than zero")
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        self.name = name
        self.batch_number = batch_number
        self.price = price

    

a=MedPlus("tanisha",17,98) 
print(a.price)
