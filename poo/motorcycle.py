from poo.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, qtd_passengers, *args):
        super(Motorcycle, self).__init__(*args)
        self.qtd_passengers = qtd_passengers

    def to_fuel(self, qtd_fuel: int):
        print('the method was called from the motorcycle class ')
        if qtd_fuel >= 30:
            print('the motorcycle fuel tank is full')
        self._qtd_fuel += qtd_fuel

    def to_paint(self, color: str):
        if color == "blue":
            print("the motorcycle can't be blue")
        self.color = color
