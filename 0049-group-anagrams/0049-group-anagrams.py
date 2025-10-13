class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initialise the dictionary
        res = {}
        #loop through the input
        for word in strs:
            #sort the words, so that we have standard key for anagrams
            key = ("").join(sorted(word))
            #if key is not in result, initialise it
            if key not in res:
                res[key] = []
            #append the word to the key
            res[key].append(word)
        #return the ans in a list
        return list(res.values())