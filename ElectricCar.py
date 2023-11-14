from Car import Car

class ElectricCar(Car):
    def __init__(self,make_model:str="None assigned",num_doors:int=4,max_passengers:int=5) -> None:
        super().__init__(make_model,num_doors,max_passengers)

    def __str__(self) -> str:
        return f'{super().__str__()}\nELECTRIC CAR'
    
if __name__=='__main__':
    car1=ElectricCar()
    print(car1)