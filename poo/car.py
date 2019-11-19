

class Car:

    def __init__(self, color, qtd_doors, type_fuel, power, qtd_fuel, is_on, velocity):
        self.color = color
        self.qtd_doors = qtd_doors
        self.type_fuel = type_fuel
        self.power = power
        self.qtd_fuel = qtd_fuel
        self.is_on = is_on
        self.velocity = velocity

    # abastercer
    def to_fuel(self, qtd_fuel):
        self.qtd_fuel += qtd_fuel

    # ligar
    def turn_on(self):
        if self.is_on:
            print('the car is already on!!!')
        else:
            self.is_on = True
            print('the car is on!')

    def turn_off(self):
        if not self.is_on:
            print('the car is already off!!')
        else:
            self.is_on = False
            print('the car is off')

    def speed_up(self, velocity=10):
        if self.is_on:
            self.velocity += velocity
        else:
            print('to speed up the car needs to be on!!')

    def verify_batery(self):
        pass

    def verify_board_computer(self):
        pass
