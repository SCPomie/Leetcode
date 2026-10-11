class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        #base case if endword is not in wordList then return 
        if endWord not in wordList:
            return 0

        
        #create the dictionary to store the information
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        #initialise the visist and the queue
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        #start the bfs
        while q:
            for i in range(len(q)):
                word = q.popleft()
                #base case if the word matches return
                if word == endWord:
                    return res
                #goes through the word, swap them into the corresponding patterns
                #e.g dog = *og, d*g, do*
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    #checks the dictionary
                    for neiWord in nei[pattern]:
                        #if it is not in visited, add them into visited and then append to queue
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
        
            res += 1
        return 0