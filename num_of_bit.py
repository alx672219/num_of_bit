class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")   # bin() output is binary string: therefore, you need ""