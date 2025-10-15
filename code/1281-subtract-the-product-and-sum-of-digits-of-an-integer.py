class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda x, y : x * y, [int(i) for i in str(n)]) - sum([int(i) for i in str(n)])
