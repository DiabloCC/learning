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


def main():
    # test_pupil()
    test_car()

if __name__ == '__main__':
    main()
