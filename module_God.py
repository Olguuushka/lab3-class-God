#декоратор wrapper-функция, выполняющая определенные действия перед или после вызова исходной функции
def god_decorator(func):
    def wrapper(self,*args, **kwargs):# с такими параметрами декоратор может применяться для функций с произвольным числом аргументов
        print(f"Вы осмелились потревожить {self.name}")
        return func(self,*args, **kwargs)
    return wrapper

class God:

    __name=0
    __element=0
    def __init__(self, name,element):#инициализатор
        self.__name=name
        self.__element=element

    @property#Декоратор property превращает метод в свойство
    def name(self):#геттер имени
        return self.__name


    @property
    @god_decorator
    def element(self):#геттер стихии
        return self.__element


    @name.setter
    @god_decorator
    def name(self, value):  # сеттер имени
        self.__name = value


    @element.setter
    @god_decorator
    def element(self, value):#сеттер стихии
        self.__element = value

    @god_decorator
    def listen_to_prayer(self,prayer):#метод выслушать молитву
        pass

    @god_decorator
    def __str__(self):#метод приведения к строке
        return f"Бог {self.__name} стихии {self.__element}"

    @god_decorator
    def __del__(self):#деструктор
        del self

