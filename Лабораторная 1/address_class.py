import doctest


class Address:
    def __init__(self, name: str, street: str, house: int, apartment: int):
        """
        Инициализация экземпляра класса.

        :param name: Имя человека
        :param street: Улица
        :param house: Дом
        :param apartment: Квартира

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        """

        self.name = name
        self.street = street
        self.house = house
        self.apartment = apartment

    @property
    def name(self):
        """
        Геттер для поля name

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.name
        'Петров А. А.'
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Сеттер для поля name

        :param name: Новый человек

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.name = 'Петров А. А.'
        >>> address.name
        'Петров А. А.'
        """
        if not isinstance(name, str):
            raise TypeError("Name must be str.")
        if len(name) == 0:
            raise ValueError("Name must be not empty.")
        self.__name = name

    @property
    def street(self):
        """
        Геттер для поля street

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.street
        'Новороссийская'
        """
        return self.__street

    @street.setter
    def street(self, street: str):
        """
        Сеттер для поля street

        :param street: Новая улица

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.street = 'Новороссийская'
        >>> address.street
        'Новороссийская'
        """
        if not isinstance(street, str):
            raise TypeError("Street must be str.")
        if len(street) == 0:
            raise ValueError("Street must be not empty.")
        self.__street = street

    @property
    def house(self):
        """
        Геттер для поля house

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.house
        15
        """
        return self.__house

    @house.setter
    def house(self, house: int):
        """
        Сеттер для поля house

        :param house: Новый дом

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.house = 15
        >>> address.house
        15
        """
        if not isinstance(house, int):
            raise TypeError("House must be int.")
        if house <= 0:
            raise ValueError("House must be more than 0.")
        self.__house = house

    @property
    def apartment(self):
        """
        Геттер для поля apartment

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.apartment
        85
        """
        return self.__apartment

    @apartment.setter
    def apartment(self, apartment: int):
        """
        Сеттер для поля apartment

        :param apartment: Новая квартира

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address.apartment = 85
        >>> address.apartment
        85
        """
        if not isinstance(apartment, int):
            raise TypeError("Apartment must be int.")
        if apartment <= 0:
            raise ValueError("Apartment must be more than 0.")
        self.__apartment = apartment

    def __str__(self):
        """
        Возвращает отформатированную строку с информацией о книге.

        >>> address = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> str(address)
        'Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85)'
        """
        return f'Имя: "{self.name}" (Адрес: улица {self.street}, дом {self.house}, квартира {self.apartment})'


if __name__ == '__main__':
    doctest.testmod()
