import unittest
from rk1 import task_1, task_2, task_3, streets, houses, houses_streets

one_to_many = [(h.number, h.floor, s.name)
                   for s in streets
                   for h in houses
                   if h.street_id == s.id]

many_to_many_temp = [(s.name, hs.street_id, hs.house_id)
                         for s in streets
                         for hs in houses_streets
                         if s.id == hs.street_id]

many_to_many = [(h.number, h.floor, street_name)
                    for street_name, street_id, house_id in many_to_many_temp
                    for h in houses if h.id == house_id]

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(task_1(streets, one_to_many), [('Академическая', [7, 45]), ('Арбат', [71])])

    def test2(self):
        self.assertEqual(task_2(streets, one_to_many), [('Арбат', 21), ('Тверская', 16), ('Академическая', 11)])

    def test3(self):
        self.assertEqual(task_3(many_to_many), [('Академическая', 26), ('Академическая', 71), ('Арбат', 23),
                                                ('Коптевская', 26), ('Коптевская', 45), ('Михалковская', 23),
                                                ('Михалковская', 7), ('Спасская', 71), ('Тверская', 23),
                                                ('Тверская', 45)])

if __name__ == '__main__':
    unittest.main()
