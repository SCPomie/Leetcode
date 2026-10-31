class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)

        #check whether a valid arrangement is possible
        if max(counts.values()) > (n + 1) // 2:
            return ""
        #builts the answer
        res = [""] * n
        #set the index to 0
        index = 0
        #gets the character : counts
        for char, count in counts.most_common():
            #adds the character the the index
            #after the first loop the most common one is done, when the second loop starts it would start at 1,3,5 which is the missing spaces
            #after the first loop of 0,2,4
            for _ in range(count):
                #when the index is over the length of the string, then reset it to 1
                if index >= n:
                    index = 1
                #adds the answer the the index and increment by 2
                res[index] = char
                index += 2
        #joins the answer
        return "".join(res)
