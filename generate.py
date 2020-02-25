class Solution:
    def generate(self, n):
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
        if left < n:
            self._gen(left + 1, right, n, result + '(')
        if right < left and right < n:
            self._gen(left, right + 1, n, result + ')')


n = 3
print(Solution().generate(n))
