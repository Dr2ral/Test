import unittest
from unittest import TestCase
import student
class Test(TestCase):

    def test_walk(self):
        self.assertEqual(pers1.walk(), 500,f'Дистанции не равны {pers1.distance} != 500')

    def test_run(self):
        self.assertEqual(pers2.run(), 1000, f'Дистанции не равны {pers2.distance} != 1000')

    def test_wr(self):
        self.assertEqual(pers1.walk(), pers2.run(), f'{pers2} должен преодолеть дистанцию больше, чем {pers1}.')



pers1 = student.Student('Kolek')
pers2 = student.Student('Vasek')

if __name__ == '__main__':
    unittest.main()

