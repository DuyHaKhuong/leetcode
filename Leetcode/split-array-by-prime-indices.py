"""
3618. Split Array by Prime Indices
You are given an integer array nums.

Split nums into two arrays A and B using the following rule:

Elements at prime indices in nums must go into array A.
All other elements must go into array B.
Return the absolute difference between the sums of the two arrays: |sum(A) - sum(B)|.

Note: Indices are 0-based; primes are 2, 3, 5, ...
"""
from typing import List
import math
import numpy as np 


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        if len(nums) < 2:
            return abs(sum_all)
        sum_prime = 0
        for k in range(2, len(nums)):
            if nums[k] is None: # composite number
                continue
            sum_prime += nums[k]
            for m in range(k*k, len(nums), k):
                nums[m] = None
        return abs(sum_all - 2*sum_prime)

    def splitArrayOld(self, nums: List[int]) -> int:
        is_prime = self.sieve2(len(nums))
        sum_prime_idx = sum(num for i, num in enumerate(nums) if is_prime[i])
        sum_comp_idx = sum(num for i, num in enumerate(nums) if not is_prime[i])
        return abs(sum_comp_idx - sum_prime_idx)

    @classmethod
    def sieve(cls, N):
        # Handle small N explicitly to avoid IndexError when N < 2
        if N < 2:
            return [False] * (N + 1)

        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False
        # Standard sieve, start crossing off at k*k
        for k in range(2, int(math.isqrt(N)) + 1):
            if is_prime[k]:
                step_start = k * k
                for m in range(step_start, N + 1, k):
                    is_prime[m] = False
        return is_prime

    @classmethod
    def sieve2(cls, N):
        is_prime = np.ones(N + 1, dtype=bool)
        is_prime[:2] = False
        for k in range(2, int(math.isqrt(N)) + 1):
            if not is_prime[k]:
                continue
            is_prime[k*k::k] = False
        return is_prime

        


if __name__ == "__main__":
    import time

    sol = Solution()

    # Small correctness tests
    tests = [
        # nums, expected |sum(A) - sum(B)|, note: prime indices are 2,3,5,...
        ([1, 2, 3, 4, 5], 1),  # A: [3,4] (idx 2,3) -> 7, B: [1,2,5] -> 8
        ([], 0),               # Empty array -> 0
    ]
    for i, (nums, expected) in enumerate(tests, 1):
        got = sol.splitArray(nums)
        print(f"Test {i}: got={got}, expected={expected}")
        assert got == expected, f"Test {i} failed: got {got}, expected {expected}"

    # Performance test on a large array
    n = 2000_000  # adjust if needed
    large = list(range(n))  # simple deterministic data
    t0 = time.perf_counter()
    result = sol.splitArray(large)
    t1 = time.perf_counter()
    elapsed_ms = (t1 - t0) * 1000
    print(f"Performance: n={n}, result={result}, time={elapsed_ms:.2f} ms")
