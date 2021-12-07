import sys
import unittest
from pathlib import Path
import context
from collections import Counter
from functools import reduce
import time
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    param_list = [([1,10,12]), ([1,2,3,4,5,6,7,8,9,10]), ([1,2,3,8,9,10])]

    def test_approaches(self):
        #   Test: if I assume the answer is always one of the positions in the set, is that always correct?
        #   Test a case where the midpoint is not in the set: e.g. a set skewed to 1 side: 1,10,12            
        
        def fn1(input):
            cnt = Counter(input)
            print(cnt)
            totals = []
            for c1 in range(min(cnt), max(cnt)+1):
                totals.append(reduce((lambda tot, next: tot if next == c1 else tot+abs(next-c1)*cnt[next]), cnt,0))
            return totals
        
        def fn2(input):
            cnt = Counter(input)
            print(cnt)
            totals = []
            for c1 in cnt:
                totals.append(reduce((lambda tot, next: tot if next == c1 else tot+abs(next-c1)*cnt[next]), cnt,0))
            return totals

        for input in self.param_list:
            with self.subTest(msg=f'Testing {input}:', input=input):
                totals1 = fn1(input)
                totals2 = fn2(input)
                self.assertEqual(min(totals1), min(totals2))        