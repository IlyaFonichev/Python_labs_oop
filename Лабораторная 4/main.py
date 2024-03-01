if __name__ == "__main__":
    # Класс Vehicle представляет базовую модель транспортного средства
    class Vehicle:
        # Конструктор класса
        def __init__(self, make: str, model: str) -> None:
            """Инициализация экземпляра класса Vehicle."""
            self._make = make  # Производитель автомобиля
            self._model = model  # Модель автомобиля

        # Метод возвращает строковое представление объекта
        def __str__(self) -> str:
            """Возвращает строковое представление автомобиля."""
            return f"{self._make} {self._model}"

        # Метод возвращает строковое представление объекта для отладки
        def __repr__(self) -> str:
            """Возвращает строковое представление объекта для отладки."""
            return f"Vehicle({self._make}, {self._model})"

    # Класс Car наследуется от Vehicle и представляет легковой автомобиль
    class Car(Vehicle):
        # Конструктор класса
        def __init__(self, make: str, model: str, doors: int) -> None:
            """Инициализация экземпляра класса Car."""
            super().__init__(make, model)
            self._doors = doors  # Количество дверей

        # Перегруженный метод для получения строкового представления автомобиля
        def __str__(self) -> str:
            """Возвращает строковое представление автомобиля с количеством дверей."""
            return super().__str__() + f" with {self._doors} doors"

    # Класс Truck наследуется от Vehicle и представляет грузовой автомобиль
    class Truck(Vehicle):
        # Конструктор класса
        def __init__(self, make: str, model: str, payload: float) -> None:
            """Инициализация экземпляра класса Truck."""
            super().__init__(make, model)
            self._payload = payload  # Грузоподъемность в тоннах

        # Перегруженный метод для получения строкового представления автомобиля
        def __str__(self) -> str:
            """Возвращает строковое представление автомобиля с грузоподъемностью."""
            return super().__str__() + f" with a payload capacity of {self._payload} tons"

    # Создание экземпляров легкового и грузового автомобилей
    my_car = Car("Toyota", "Corolla",  4)
    my_truck = Truck("Mercedes-Benz", "Actros",  10)

    # Вывод информации об автомобилях
    print(my_car)  # Вывод: Toyota Corolla with  4 doors
    print(my_truck)  # Вывод: Mercedes-Benz Actros with a payload capacity of  10 tons

    pass
