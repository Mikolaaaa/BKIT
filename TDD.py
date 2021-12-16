import unittest
import sys, os
sys.path.append(os.getcwd())
from main import *


class Testget_B123(unittest.TestCase):
    def test_B1(self):
        one_to_many = [(f.name, f.size, d.name)
                       for d in File_dirs
                       for f in Files
                       if f.dir_id == d.id]
        self.assertEqual(B1(one_to_many), [('Демидович учебник', 59836, 'учёба'), ('конспект', 4036, 'учёба'),
                                           ('Крым', 4036, 'отдых'), ('Лаба3', 2638, 'учёба'), ('программы', 9836, 'телефон'),
                                           ('Резерваная копия', 349803, 'телефон'), ('Турция', 12089, 'отдых')])


    def test_B2(self):
        one_to_many = [(f.name, f.size, d.name)
                        for d in File_dirs
                        for f in Files
                        if f.dir_id == d.id]
        self.assertEqual(B2(one_to_many), [('учёба', 3), ('отдых', 2), ('телефон', 2)])

    def test_B3(self):
        many_to_many_temp = [(d.name, fd.Filedir_id, fd.File_id)
                             for d in File_dirs
                             for fd in File_dir_File
                             if d.id == fd.Filedir_id]
        many_to_many = [(f.name, f.size, dir_name)
                        for dir_name, dir_id, File_id in many_to_many_temp
                        for f in Files if f.id == File_id]
        self.assertEqual(B3(many_to_many),{ 'Резерваная копия' : ['телефон', 'телефон (другой)'], 'Турция' : ['отдых', 'отдых (другой)']})

if __name__ == '__main__':
    unittest.main()