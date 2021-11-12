from unittest import TestCase
import hello

class TestHello(TestCase):
    
    def test_hello_add(self):
        self.assertEqual(4, hello.add(3))
        