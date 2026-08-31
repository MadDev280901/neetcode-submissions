import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def get_children(lock):
            res = []
            for i in range(4):
                # Rotate wheel forward
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                
                # Rotate wheel backward
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = collections.deque()
        q.append(("0000", 0))  # (current_lock_state, turns)
        visit = set(deadends)
        
        while q:
            lock, turns = q.popleft()
            
            if lock == target:
                return turns
                
            for child in get_children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
                    
        return -1