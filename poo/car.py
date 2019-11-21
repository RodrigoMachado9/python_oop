from poo.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, qtd_doors, *args):
        super(Car, self).__init__(*args)
        self.qtd_doors = qtd_doors
