"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = collections.Counter(s)
        out = ""
        heap = []
        for key, value in c.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        while len(heap) > 1:
            value, key = heapq.heappop(heap)
            value1, key1 = heapq.heappop(heap)
            out += key
            out += key1
            if value != -1:
                heapq.heappush(heap, (value+1, key))
            if value1 != -1:
                heapq.heappush(heap, (value1+1, key1))
        if heap:
            value, key = heapq.heappop(heap)
            if value == -1:
                out += key
                return out
            return ""
        return out
