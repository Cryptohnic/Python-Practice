from Car import Car

class GasolineCar(Car):
    def __init__(self,make_model:str="None assigned",num_doors:int=4,max_passengers:int=5,gas_tank_size:int=-1) -> None:
        super().__init__(make_model,num_doors,max_passengers)
        self.gas_tank_size=gas_tank_size
    
    def get_gas_tank_size(self) -> int:
        return self.gas_tank_size
    
    def set_gas_tank_size(self,size:int) -> None:
        self.gas_tank_size=size
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nGas tank size: {self.gas_tank_size}'
    

if __name__=='__main__':
    car1=GasolineCar()
    car1.set_gas_tank_size(10)
    print(car1.get_gas_tank_size())
    print(car1)