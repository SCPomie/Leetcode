class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordDict = set(wordDict)
        def dfs(i):
            #nbase case when you reach the end of the string, append the current words to the final result
            if i == len(s):
                return result.append((" ").join(current))
            #iterates through the current index to the end of the string
            for j in range(i, len(s)):
                #if the word is in the dictionary
                if s[i: j + 1] in wordDict:
                    current.append(s[i: j + 1])
                    #recursive backtracking calls from the end of the current word
                    dfs(j + 1)
                    #pops the latest word, so that backtracking can collect other words when the path for the current word is done
                    current.pop()
    
        
        #the temporal word holder
        current = []
        #findal result
        result = []
        #calls the dfs for backtracking
        dfs(0)
        return result
