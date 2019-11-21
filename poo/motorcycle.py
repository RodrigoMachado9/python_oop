from poo.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, qtd_passengers, *args):
        super(Motorcycle, self).__init__(*args)
        self.qtd_passengers = qtd_passengers