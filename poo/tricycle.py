import poo.vehicle as vehicle, poo.motorcycle as motorcycle

# multiple herance,
# about inherits the father class,  see below!
# as the daughter class already inherits the parent class, it is not necessary to inherit the parent class
class Tricycle(motorcycle.Motorcycle):
    def __init__(self, *args):
        super(Tricycle, self).__init__(*args)

instante_tricycle = Tricycle(2,'GREEN', 'GASOLINE', '500').velocity = 2
print(instante_tricycle)
