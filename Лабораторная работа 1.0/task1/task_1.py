import doctest
from typing import Union


class Tables:
    def __init__(self, material: str, weight: Union[int, float]):
        if not isinstance(material, str):
            raise TypeError("Материал стола должен описан словесно")
        if not weight > 0:
            raise ValueError("Вес стола не может быть меньше 0")
        # Атрибутам присваиваются значения аргументов конструктора объектов
        self.material = material
        self.weight = weight

    def material_description(self, material: str) -> str:
        """
        :return: Материал стола
        Примеры:
        >>> wood_table = Tables("Дерево", 10)
        >>> wood_table.material_description
        """
        return f"Материал стола - {material}"

    def weight_description(self, weight: Union[int, float]) -> str:
        """
        :return: Вес стола
        Примеры:
        >>> wood_table = Tables("Дерево", 10)
        >>> wood_table.weight_description
        """
        return f"Вес стола - {weight}"


class Books:
    def __init__(self, author: str, page_number: int, genre: str):
        if not isinstance(author, str):
            raise TypeError("Наименование автора должно словесным")
        if not page_number > 0 and isinstance(page_number, float):
            raise ValueError("Число страниц должно быть целым числом и больше 0")
        if not isinstance(genre, str):
            raise TypeError("Наименование жанра книги должно словесным")
        # Атрибутам присваиваются значения аргументов конструктора объектов
        self.author = author
        self.page_number = page_number
        self.genre = genre

    def author(self, author: str) -> str:
        # Даётся краткая сводка по автору книги
        """
        :return: Краткая сводка по автору книги
        Примеры:
        >>> Idiot = Books("Достоевский", 640, "Роман")
        >>> Idiot.author
        """
        ...

    def page_number(self, page_number: int) -> int:
        # Выводится число страниц в данной книге
        """
        :return: Число страниц в данной книге
        Примеры:
        >>> Idiot = Books("Достоевский", 640, "Роман")
        >>> Idiot.page_number
        """
        ...

    def genre(self, genre: str) -> str:
        # Даётся краткая сводка по жанру книги
        """
        :return: Краткая сводка по жанру книги
        Примеры:
        >>> Idiot = Books("Достоевский", 640, "Роман")
        >>> Idiot.genre
        """
        ...


class consumption_indicator:
    def __init__(self, distance: Union[int, float], available_fuel: Union[int, float], consumption_per_km: Union[int, float]):
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно указываться числом")
        if not distance > 0:
            raise ValueError("Расстояние должно быть указано положительным числом")
        if not isinstance(available_fuel, (int, float)):
            raise TypeError("Доступный объем топлива должен указываться числом")
        if not available_fuel > 0:
            raise ValueError("Доступный объем топлива должен быть указан положительным числом")
        if not isinstance(consumption_per_km, (int, float)):
            raise TypeError("Расход на 100 км должен указываться числом")
        if not consumption_per_km > 0:
            raise ValueError("Расход на 100 км должен быть указан положительным числом")
        # Атрибутам присваиваются значения аргументов конструктора объектов
        self.distance = distance
        self.available_fuel = available_fuel
        self.consumption_per_km = consumption_per_km

    def required_fuel_for_route(self, consumption_per_km: Union[int, float], distance: Union[int, float]) -> (int, float):
        # Вычисляется необходимое количество топливо для построенного маршрута с учетом расхода автомобиля
        """
        :required_fuel: необходимое кол-во топливо на маршрут с учетом расхода топлива автомобилем
        :return: Выдает значение требуемого значения топлива на маршрут с учетом расхода топлива автомобилем
        Примеры:
        >>> Car = consumption_indicator(100, 81, 9.5)
        >>> Car.required_fuel_for_route
        """
        ...

    def comparing_necessary_and_available_fuel(self, available_fuel: Union[int, float]) -> bool:
        # Выдается информация о том, хватает ли текущего запаса на заданную дистанцию.
        """
        :return: Выдает информацию хватит ли имеющегося топлива на совершаемый маршрут
        Примеры:
        >>> Car = consumption_indicator("Тест", 81, 9.5)
        >>> Car.comparing_necessary_and_available_fuel
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    
