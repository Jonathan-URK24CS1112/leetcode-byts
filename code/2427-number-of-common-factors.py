class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        num = min(a, b)
        other = max(a, b)

        count = 0
        for i in range(1, num + 1):
            if num % i == 0 and other % i == 0:
                count += 1

        return count
