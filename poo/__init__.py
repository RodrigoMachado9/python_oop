from poo.car import Car
from poo.motorcycle import Motorcycle

if __name__ == '__main__':
    print('\n')
    uno_red = Car(4, 'red', 'flex', 2.0)
    uno_red.turn_on()
    uno_red.to_fuel(10)
    # print("uno-red: the amount of fuel is: %s" % uno_red.qtd_fuel)
    del uno_red

    print('\n')
    motorcycle_red = Motorcycle(2, 'red', 'flex', 2.0)
    motorcycle_red.turn_on()
    # print(motorcycle_red.is_on)
    print('\nplaying with polymorphism > by motorcycle ')
    motorcycle_red.to_fuel(31)
    print('\nplaying with polymorphism > by car ')
    uno_purple = Car(4, 'purple', 'flex', 2.0)
    uno_purple.to_fuel(2)
    # print(uno_purple.qtd_fuel)

    # uno_black = Car(2, 'black', 'gasoline', 1.4)
    # # uno_black.turn_off()
    # uno_black.turn_on()
    # uno_black.to_fuel(5)
    # print("uno-black: the amount of fuel is: %s" % uno_black.qtd_fuel)
    # uno_black.speed_up(10)
    # print(uno_black.velocity)
    # print('\n')
    # # help(uno_black.to_fuel) # native function help,  is responsible to show docstring and method name!
