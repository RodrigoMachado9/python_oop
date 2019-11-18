

class Car:

    def __init__(self, color, qtd_doors, type_fuel, power, qtd_fuel, is_on):
        self.color = color
        self.qtd_doors = qtd_doors
        self.type_fuel = type_fuel
        self.power = power
        self.qtd_fuel = qtd_fuel
        self.is_on = is_on

    #abastercer
    def tofuel(self):
        self.qtd_fuel += 20

    #ligar
    def  turnon(self):
        if self.is_on:
            print('the car is on!')
        else:
            self.is_on = True

    def turnoff(self):
        if not self.is_on:
            print('the car is off')
        else:
            self.is_on = False

    def verify_batery(self):
        pass

    def verify_board_computer(self):
        pass