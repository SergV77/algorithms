from typing import List
from collections import OrderedDict

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = OrderedDict()
        for i in range(m):
            perm[i+1] = i



        ans = []

        for el in queries:
            pos = perm[el]
            ans.append(pos)
            # for i in len(pos):



        return  ans



if __name__ == '__main__':
    queries = [3, 1, 2, 1]
    m = 5
    print(Solution().processQueries(queries, m))