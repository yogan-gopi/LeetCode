from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        
        queue = deque()
        enqueued = {start}
        queue.append((start, 0))
        
        while queue:
            gene, level = queue.popleft()
            if gene == end:
                return level
            
            for i in range(8):
                for j in "ACGT":
                    newGene = gene[:i] + j + gene[i+1:]
                    
                    if newGene not in enqueued and newGene in bank:
                        queue.append((newGene, level+1))
                        enqueued.add(newGene)
        return -1