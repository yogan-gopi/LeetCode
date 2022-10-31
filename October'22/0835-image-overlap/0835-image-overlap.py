class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        res = {}
        i1 = []
        i2 = []
        
        for i in range(len(img2)):
            for j in range(len(img2[i])):
                if img2[i][j] == 1:
                    i2.append([i, j])
                if img1[i][j] == 1:
                    i1.append([i, j])
        for i in i1:
            for j in i2:
                n = "{}, {}".format(j[0]-i[0], j[1]-i[1])
                if n not in res:
                    res[n] = 0
                res[n] += 1
        maxi = 0
        for i in res:
            if res[i] > maxi:
                maxi = res[i]
        return maxi
            
            