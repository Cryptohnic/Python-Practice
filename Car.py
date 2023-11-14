class Car:
    def __init__(self,make_model:str="None assigned",num_doors:int=4,max_passengers:int=5) -> None:
        self.make_model=make_model
        self.num_doors=num_doors
        self.max_passengers=max_passengers

    def set_make_model(self, make_model:str) -> None:
        self.make_model=make_model

    def get_make_model(self) -> str:
        return self.make_model
    
    def set_num_doors(self,num_doors:int) -> None:
        self.num_doors=num_doors

    def get_num_doors(self) -> int:
        return self.num_doors
    
    def set_max_passengers(self,max_passengers:int) -> None:
        self.max_passengers=max_passengers

    def get_max_passengers(self) -> int:
        return self.max_passengers 
    
    def __str__(self) -> str:
        return  f'Make and Model: {self.make_model}\nNumber of doors: {self.num_doors}\nMaximum number of passengers: {self.max_passengers}'

# print('If this code prints when running ElectricCar.py or GasolineCar.py, all code gets ran when importing a file')

if __name__=='__main__':
    car1=Car()
    car1.set_make_model("Dodge Dart")
    print(car1.get_make_model())
    print(car1)
    print(f'__name__ inside Car.py if __name__==\'__main__\': {__name__}')
else:
    print(f'__name__ inside Car.py if not __name__==\'__main__\': {__name__}')
    print('Importing a file runs all of the code in it that isn\'t in if __name__==\'__main__\' and intializes all functions')