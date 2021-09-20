#!/usr/bin/env python

import unittest

from Ad1 import q1


class Test_q1(unittest.TestCase):

    def test_init(self):
        assert 5 == 5   
  
    def test_impar_numero(self):
        assert ((q1.main(3))[0]) == 3 
        
    def test_impar_area(self):
        assert round(((q1.main(3))[1]),2) == 28.27 
        
    def test_impar_perimetro(self):
        assert round(((q1.main(3))[2]),2) == 18.85     
        
    def test_par(self):
        assert q1.main(2) == 2



if __name__ == '__main__':
    unittest.main()
    