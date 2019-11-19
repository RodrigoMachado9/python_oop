from poo.car import Car




if __name__ == '__main__':
    print('\n')
    uno_red = Car('red', 4, 'flex', 1.0, 0, False)
    uno_red.turn_on()
    uno_red.to_fuel()
    print("uno-red: the amount of fuel is: %s" % uno_red.qtd_fuel)

    print('\n')
    uno_black = Car('black', 2, 'gasoline', 1.4, 10, False)
    uno_black.turn_off()
    uno_black.to_fuel()
    print("uno-black: the amount of fuel is: %s" % uno_black.qtd_fuel)