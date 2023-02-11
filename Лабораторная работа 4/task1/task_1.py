class Steel:
    """ Базовый класс сталей. """
    def __init__(self, name: str, tensile_strength: float, alloy_additives: str) -> None:
        self.name = name
        self.tensile_strength = tensile_strength
        self.alloy_additives = alloy_additives

    def __str__(self):
        return f"Марка стали: {self.name}. Сопротивление на расстяжение: {self.tensile_strength}. " \
               f"Легирующие добавки: {self.alloy_additives}\n"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, tensile_strength={self.tensile_strength!r})"


class Instrumental_steel(Steel):
    """ Класс инструментальных сталей. Отличается особым вниманием к времени работы от заточки до заточки """
    def __init__(self, name: str, wear_resistance: float, alloy_additives: str) -> None:
        super().__init__(name, alloy_additives)
        self.wear_resistance = wear_resistance

    def __str__(self):
        return f"Марка стали: {self.name}. Легирующие добавки: {self.alloy_additives}. " \
               f"Износостойкость: {self.wear_resistance}\n"

    def maintenance_rules(self, name: str, wear_resistance: float):
        """ Выдается перечень правил обслуживания рабочих иструментов на основе инструментальных сталей """
        ...


class Construction_steel(Steel):
    """ Класс конструкционной стали. Особый параметр - наличие короизейстокого покрытия. """
    def __init__(self, name: str, corrosion_resistance: str, alloy_additives: str) -> None:
        super().__init__(name, alloy_additives)
        self.corrosion_resistance = corrosion_resistance

    def __str__(self):
        return f"Марка стали: {self.name}. Наличие легирующих добавок: {self.alloy_additives}. " \
               f"Короизиестойкое покрытие: {self.corrosion_resistance}\n"

    def resistance_duration(self, name: str, alloy_additives: str, corrosion_resistance: str, corrosion_resistance_cover_thick: float):
        """ Расчет времени, через которое необходимо обновлять корозиестойкое покрытие """
        ...


steel1 = Steel("С235", 400.0, "Хром")
print(steel1.__str__())
print(steel1.__repr__())

