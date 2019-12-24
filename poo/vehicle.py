class Vehicle:
    """
        this class vehicle , class used to inheritance between child classes.
    """

    def __init__(self, color: str, type_fuel: str, power: int):
        self.color = color
        self.type_fuel = type_fuel
        self.power = power
        self.qtd_fuel: int = 0
        self.is_on: bool = False
        self.velocity: int = 0

    def __del__(self):
        print('object has been removed from memory!')

    # abastercer
    def to_fuel(self, qtd_fuel: int):
        """
        :param qtd_fuel: responsible for increasing a certain amount of fuel
        :return:
        """
        self.qtd_fuel += qtd_fuel

    # ligar
    def turn_on(self):
        if self.is_on:
            print('the vehicle is already on!!!')
        else:
            self.is_on = True
            print('the vehicle is on!')

    def turn_off(self):
        if not self.is_on:
            print('the vehicle is already off!!')
        else:
            self.is_on = False
            print('the vehicle is off')

    def speed_up(self, velocity: int = 10):
        if self.is_on:
            self.velocity += velocity
        else:
            print('to speed up the vehicle needs to be on!!')

    def verify_batery(self):
        pass

    def verify_board_computer(self):
        pass
