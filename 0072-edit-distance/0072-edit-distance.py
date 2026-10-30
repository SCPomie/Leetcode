class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #create the 2d dp array
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        #make the vertical border
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        #make the horizontal boarder
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        #go in reverse directions
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                #if word1[i] = word2[j], then incrase both by 1 in the dp
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    #the dp would be 1 + the minimum of the 3 movements
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        #return the final one
        return cache[0][0]