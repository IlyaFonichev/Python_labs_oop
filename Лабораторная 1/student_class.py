import doctest


class Student:
    def __init__(self, name: str, discipline: str, exam_mark: int):
        """
        Инициализация экземпляра класса.

        :param name: Имя человека
        :param discipline: Дисциплина
        :param exam_mark: Оценка за экзамен

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        """

        self.name = name
        self.discipline = discipline
        self.exam_mark = exam_mark

    @property
    def name(self):
        """
        Геттер для поля name

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.name
        'Петров А. А.'
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Сеттер для поля name

        :param name: Новый человек

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.name = 'Петров А. А.'
        >>> student.name
        'Петров А. А.'
        """
        if not isinstance(name, str):
            raise TypeError("Name must be str.")
        if len(name) == 0:
            raise ValueError("Name must be not empty.")
        self.__name = name

    @property
    def discipline(self):
        """
        Геттер для поля discipline

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.discipline
        'Высшая математика'
        """
        return self.__discipline

    @discipline.setter
    def discipline(self, discipline: str):
        """
        Сеттер для поля discipline

        :param discipline: Новая дисцеплина

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.discipline = 'Высшая математика'
        >>> student.discipline
        'Высшая математика'
        """
        if not isinstance(discipline, str):
            raise TypeError("Discipline must be str.")
        if len(discipline) == 0:
            raise ValueError("Discipline must be not empty.")
        self.__discipline = discipline

    @property
    def exam_mark(self):
        """
        Геттер для поля exam_mark

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.exam_mark
        4
        """
        return self.__exam_mark

    @exam_mark.setter
    def exam_mark(self, exam_mark: int):
        """
        Сеттер для поля exam_mark

        :param exam_mark: Новая оценка

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> student.exam_mark = 4
        >>> student.exam_mark
        4
        """
        if not isinstance(exam_mark, int):
            raise TypeError("Exam mark must be int.")
        if 5 < exam_mark <= 2:
            raise ValueError("Exam mark must be more than 0.")
        self.__exam_mark = exam_mark

    def __str__(self):
        """
        Возвращает отформатированную строку с информацией о студенте.

        >>> student = Student("Петров А. А.", "Высшая математика", 4)
        >>> str(student)
        'Имя: "Петров А. А." ( Дисцеплина: Высшая математика, Оценка за экзамен: 4)'
        """
        return f'Имя: "{self.name}" (Адрес: улица {self.discipline}, дом {self.exam_mark})'


if __name__ == '__main__':
    doctest.testmod()
