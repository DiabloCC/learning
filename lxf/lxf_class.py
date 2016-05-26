# -*- coding: utf-8 -*-
# lxf_class.py


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return __name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return __score

    def print_info(self):
        print('Name: %s\tScore: %s' % (self.__name, str(self.__score)))


class Pupil(Student):
    def set_score(self, score):
        self.__score = score
        self.__name = 'Score changed'

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        if 80 <= self.__score < 90:
            return 'B'
        if self.__score < 0:
            return 'Invalid score!'
        return 'C'

    def print_info2(self):
        print('Name: %s\nScore: %s\nGrade: %s' %
              (self.__name, str(self.__score), self.get_grade()))


def test_pupil():
    # s = input('请输入姓名')
    Mike = Pupil('Mike', 40)
    Mike.print_info()
    # This will cause errors. Because there was no _Pupil__name.
    # Mike.print_info2()
    Mike.set_score(-10)
    Mike.print_info()
    Mike.print_info2()


class Car(object):
    _color = ''

    def description(self, name):
        self.name = name
        description_string = 'This is a %s car %s.' % (self._color, self.name)
        return description_string


class BMW(Car):
    def engin(self, message):
        # this whill cause an error:
        #   'super' object has no attribute '_color'
        super(BMW, self)._color = 'black'
        print(super(BMW, self).description('BMW'))
        print(message)


def test_car():
    car1 = Car()
    car1._color = 'golden'  # 实例可以重写类属性
    print(car1.description('Skoda'))
    print('Car has attribute "name".' if hasattr(
        Car, 'name') else 'Car has no attribute "name"!')
    print('Car has attribute "_color".' if hasattr(
        Car, '_color') else 'Car has no attribute "_color"!')
    print('Car1 has attribute "name".' if hasattr(
        car1, 'name') else 'Car1 has no attribute "name"!')
    print('Car1 has attribute "_color".' if hasattr(
        car1, '_color') else 'Car1 has no attribute "_color"!')
    # print(Car.name)
    print(car1.name)


def test_super():
    car2 = BMW()
    car2.engin('The engin is more powerful than ever!')


def test_class_attribute():
    car3 = Car()
    print(car3.description('charlie'))
    Car._color = 'black'
    print('This is Car._color:\t', Car._color, id(Car._color))
    print('This is car3._color:\t', car3._color, id(car3._color))
    car3._color = 'green'
    print('This is Car._color:\t', Car._color, id(Car._color))
    print('This is car3._color:\t', car3._color, id(car3._color))
    del car3._color
    print('This is Car._color:\t', Car._color, id(Car._color))
    print('This is car3._color:\t', car3._color, id(car3._color))


class screen():
    # if __slots__ is set, the following property definition will cause error
    # __slots__ = ('name', 'id')

    # _resolution = 300

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('screen width must be an integer!')
        if value < 0:
            raise ValueError('screen width must larger than 0!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('screen height must be an integer!')
        if value < 0:
            raise ValueError('screen height must larger than 0!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


class window(screen):
    __slots__ = ('name', 'id')


def test_property():
    s = screen()
    # s.width = -1
    # s.width = '222'
    s.width = 1024
    # s.height = -32
    # s.height = 11.25
    # s.height = 'fg'
    s.height = 768
    print('s.width = %d\ts.height = %d\ts.resolution = %d' %
          (s.width, s.height, s.resolution))
    # test __slots__
    s = window()
    s.width = 1440
    s.height = 1024
    print('s.width = %d\ts.height = %d\ts.resolution = %d' %
          (s.width, s.height, s.resolution))
    s.name = 'desktop'
    s.id = 6
    print('s.name = %s\ts.id = %d' % (s.name, s.id))
    s.depth = 8


class animal(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if value == '':
            raise ValueError("Name can not be empty!")
        self._name = value

    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string!")
        if value == '':
            raise ValueError("Category can not be empty!")
        self._cate = value

    def shout(self):
        print('I\'m a %s and my name is %s.' % (self.cate, self.name))
        print('I have voice. I can make noise.')

    def child(self):
        print('I can have children just like me.')


class mammal(animal):
    def __init__(self):
        # no need to use super(). It may cause error
        # super(mammal, self).cate = 'Mammal'
        self.cate = 'Mammal'

    def child(self):
        # print('I\'m a %s.' % self.cate)
        print('I can born children and feed them with my milk.')


class bird(animal):
    def __init__(self):
        self.cate = 'Bird'

    def child(self):
        # print('I\'m a %s.' % self.cate)
        super(bird, self).child()
        print('I can lay eggs and hatch them.')


class runnable(object):
    def run(self):
        print('I can run with my legs.')


class flyable(object):
    def fly(self):
        print('I can fly with my wings.')


class dog(mammal, runnable):
    def __init__(self, name):
        # no need to use super(). It may cause error
        # super(dog, self)._name = name
        super(dog, self).__init__()
        self.name = name


class parrot(bird, flyable):
    def __init__(self, name):
        super(parrot, self).__init__()
        self.name = name


class bat(mammal, flyable):
    def __init__(self, name):
        super(bat, self).__init__()
        self.name = name


def test_mixin():
    doggie = dog('Doggie')
    doggie.shout()
    doggie.run()
    doggie.child()
    print('-------------')
    littleP = parrot('Mimi')
    littleP.shout()
    littleP.fly()
    # littleP.bornchild()
    littleP.child()
    print('-------------')
    batman = bat('Batman')
    batman.shout()
    batman.fly()
    batman.child()


def main():
    # test_pupil()
    # test_car()
    # test_super()
    # test_class_attribute()
    # test_property()
    test_mixin()

if __name__ == '__main__':
    main()
