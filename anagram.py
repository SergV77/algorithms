from typing import List

class Solution:
    def anagramMapping(self, nums1: List[int], nums2: List[int]) ->List[int]:
        mapping = [num2.index(el) for i, el in enumerate(num1)]
        return mapping

class SolutionTwo:
    def anagramMapping(self, nums1: List[int], nums2: List[int]) ->List[int]:
        num = {x: i for i, x in enumerate(num2)}
        return [num[x] for x in num1]

if __name__ == '__main__':
    num1 = [12, 28, 46, 32, 50]
    num2 = [50, 12, 32, 46, 28]
    print(Solution().anagramMapping(num1, num2))
    print(SolutionTwo().anagramMapping(num1, num2))