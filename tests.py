
import os
import unittest

from .sieve_of_eratosthenes import generate_primes, generator_cached

class TestFirstThousandPrimes(unittest.TestCase):

    def test(self):

        this_dir = os.path.dirname(os.path.abspath(__file__))
        primes_path = os.path.join(this_dir, 'thousand_primes.dat')       

        with open(primes_path,'r') as f:
            
            for prime_file, prime_sieve in zip(f, generate_primes(10**7)):
                self.assertEqual(int(prime_file), prime_sieve)


class TestGeneratorCached(unittest.TestCase):

    def test_recreates_original(self):

        N = 10
        range_cached = generator_cached(range, N)
        
        for i, j in zip(range_cached(), range(N)):
            self.assertEqual(i,j)


    def test_actually_caching(self):

        range_cached = generator_cached(range, 10)

        values = list(range_cached())

        new_generator = range_cached()
        
        self.assertSequenceEqual(values, new_generator.gi_frame.f_locals['previous_values'])


    def test_recreates_original_twice(self):

        N = 10
        range_cached = generator_cached(range, N)

        for i, j in zip(range_cached(), range(N)):
            pass
        
        for i, j in zip(range_cached(), range(N)):
            self.assertEqual(i,j)
