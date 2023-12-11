import doctest

from address_class import Address


class AddressBook:
    def __init__(self, addresses):
        """
        Инициализация экземпляра класса "AddressBook".

        :param addresses: Список адресов в книге (может быть пустым)

        >>> book = AddressBook([])
        >>> str(book)
        'AddressBook: '
        >>> address1 = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address2 = Address("Сидоров А. А.", "Новокузнецкая", 25, 185)
        >>> book = AddressBook([address1, address1])
        >>> str(book)
        'AddressBook: Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85) Имя: "Сидоров А. А." (Адрес: улица Новокузнецкая, дом 25, квартира 185)'
        """
        for address in addresses:
            if not isinstance(address, Address):
                raise TypeError("All elements in the 'addresses' list must be instances of the 'Address' class.")
        self.__addresses = addresses

    def add_address(self, address: Address):
        """
        Добавляет адрес в книгу.

        :param address: Экземпляр класса Address

        >>> book = AddressBook([])
        >>> address = Address("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.add_address(address)
        >>> str(book)
        'AddressBook: Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85)'
        """
        if not isinstance(address, Address):
            raise TypeError("The 'address' parameter must be an instance of the 'Address' class.")
        self.__addresses.append(address)

    def remove_address_by_name(self, name: str):
        """
        Удаляет адрес из книги по имени.

        :param name: Имя человека (строка)

        >>> book = AddressBook([])
        >>> address1 = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address2 = Address("Сидоров А. А.", "Новокузнецкая", 25, 185)
        >>> book.add_address(address1)
        >>> book.add_address(address2)
        >>> book.remove_address_by_name("Петров А. А.")
        >>> str(book)
        'AddressBook: Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85)'
        """
        if not isinstance(name, str):
            raise TypeError("The 'name' parameter must be a string.")

        for address in self.__addresses:
            if address.title == name:
                self.__addresses.remove(address)
                return

        raise ValueError(f"No address with the name '{name}' found on the book.")

    def get_address_count(self):
        """
        Возвращает количество адресов в книге.

        :return: Целое число, представляющее количество адресов в книге.

        >>> book = AddressBook([])
        >>> book.get_address_count()
        0
        >>> address1 = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address2 = Address("Сидоров А. А.", "Новокузнецкая", 25, 185)
        >>> book.add_address(address1)
        >>> book.add_address(address2)
        >>> book.get_address_count()
        2
        """
        return len(self.__addresses)

    @property
    def addresses(self):
        """
        Геттер для приватного поля addresses.

        >>> address1 = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address2 = Address("Сидоров А. А.", "Новокузнецкая", 25, 185)
        >>> book = AddressBook([address1, address2])
        >>> for i in book.addresses:
        ...     print(i)
        Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85)
        Имя: "Сидоров А. А." (Адрес: улица Новокузнецкая, дом 25, квартира 185)
        """
        return self.__addresses

    def __str__(self):
        """
        Возвращает отформатированную строку с информацией об адресной книге.

        >>> address1 = Address("Петров А. А.", "Новороссийская", 15, 85)
        >>> address2 = Address("Сидоров А. А.", "Новокузнецкая", 25, 185)
        >>> book = AddressBook([address1, address2])
        >>> str(book)
        'AddressBook: Имя: "Петров А. А." (Адрес: улица Новороссийская, дом 15, квартира 85) Имя: "Сидоров А. А." (Адрес: улица Новокузнецкая, дом 25, квартира 185)'
        """
        return f'AddressBook: {" ".join(str(address) for address in self.addresses)}'

    if __name__ == '__main__':
        doctest.testmod()
