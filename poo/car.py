from poo.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, qtd_doors, *args):
        super(Car, self).__init__(*args)
        self.qtd_doors = qtd_doors


    def to_fuel(self, qtd_fuel):
        print('the method was called from the car class')
        self.qtd_fuel += qtd_fuel