import unittest
from primes import prime_decomposition

class TestAssignment1(unittest.TestCase):
    def test_prime_decomposition_empty_case_is_correct(self):
        self.assertEqual(prime_decomposition(0),[])
    
    def test_prime_decomposition_prime_case_is_correct(self):
        self.assertEqual(prime_decomposition(13),[13])

    def test_prime_decomposition_repeating_factors_case_is_correct(self):
        self.assertEqual(prime_decomposition(8),[2,2,2])
    
    def test_prime_decomposition_no_repeating_factors_case_is_correct(self):
        self.assertEqual(prime_decomposition(55),[5,11])

if __name__=='__main__':
    unittest.main()