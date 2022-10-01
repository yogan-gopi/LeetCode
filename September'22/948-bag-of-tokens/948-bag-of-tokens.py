class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        
        l , r = 0, (len(tokens)-1)
        score = 0

        
        while l <= r and (score or power >= tokens[l]):
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l+=1
                
            elif l != r:
                power += tokens[r]
                score -= 1
                r -= 1
            
            else:
                break
        return score
                
            