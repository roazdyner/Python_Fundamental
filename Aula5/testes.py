#!/usr/bin/python3
import unittest

def soma(n1,n2):
    return n1+n2

def subtrai(n1,n2):
    return n1 - n2

print('Oi estou sendo executado')

class Testes(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(8,2),10)
        self.assertLess(soma(5,5),12)

    def teste_subtrai(self):
        self.assertEqual(subtrai(10,2),8)
        self.assertGreater(subtrai(10,4),3)


if __name__ == '__main__':
    #assert soma(3,5) == 5, "modulo somar falhou"
    unittest.main()