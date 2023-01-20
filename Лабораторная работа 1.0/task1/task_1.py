import doctest


class Tables:
    def __init__(self, material: str, weight: float):
        if not isinstance(material, str):
            raise TypeError("Материал стола должен описан словесно")
        if not weight > 0:
            raise ValueError("Вес стола не может быть меньше 0")
        # Атрибутам присваиваются значения аргументов конструктора объектов
        self.material = material
        self.weight = weight

    def material_description(self):
        print(f"Материал стола - {self.material}")

    def weight_description(self):
        print(f"Вес стола - {self.weight}")


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

    def author(self) -> str:
        # Даётся краткая сводка по автору книги
        ...

    def page_number(self) -> int:
        # Выводится число страниц в данной книге
        ...

    def genre(self) -> str:
        # Даётся краткая сводка по жанру книги
        ...


class consumption_indicator:
    def __init__(self, distance, available_fuel, consumption_per_km: float):
        if not isinstance(distance, float):
            raise TypeError("Расстояние должно указываться числом")
        if not distance > 0:
            raise ValueError("Расстояние должно быть указано положительным числом")
        if not isinstance(available_fuel, float):
            raise TypeError("Доступный объем топлива должен указываться числом")
        if not available_fuel > 0:
            raise ValueError("Доступный объем топлива должен быть указан положительным числом")
        if not isinstance(consumption_per_km, float):
            raise TypeError("Расход на 100 км должен указываться числом")
        if not consumption_per_km > 0:
            raise ValueError("Расход на 100 км должен быть указан положительным числом")
        # Атрибутам присваиваются значения аргументов конструктора объектов
        self.distance = distance
        self.available_fuel = available_fuel
        self.consumption_per_km = consumption_per_km

    def required_fuel_for_route(self) -> int:
        # Вычисляется необходимое количество топливо для построенного маршрута с учетом расхода автомобиля
        ...

    def comparing_necessary_and_available_fuel(self) -> bool:
        # Выдается информация о том, хватает ли текущего запаса на заданную дистанцию.
        ...


if __name__ == "__main__":
    doctest.testmod()
