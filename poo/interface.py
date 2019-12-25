from abc import abstractclassmethod, ABC


class Interface(ABC):

    @abstractclassmethod
    def to_fuel(self, qtd_fuel: int):           # assinatura
        pass

    @abstractclassmethod
    def turn_on(self):                          # assinatura
        pass

    @abstractclassmethod
    def turn_off(self):                         # assinatura
        pass

    @abstractclassmethod
    def speed_up(self, velocity: int = 10):     # assinatura
        pass

    @abstractclassmethod
    def to_paint(self, color: str):             # assinatura
        pass