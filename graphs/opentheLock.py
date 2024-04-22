"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1)%10)
                res.append(lock[:i]+ digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10 )%10)
                res.append(lock[:i]+ digit + lock[i+1:])

            return res
        
        q = deque()
        q.append(['0000', 0])
        visited = set(deadends)
        while q:
            lock ,turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    q.append([child, turns+1])
                    visited.add(child)
        return -1