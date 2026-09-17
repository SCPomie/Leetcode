from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # get the length of the word and also the length of the sliding windows
        word_len = len(words[0])
        window_len = word_len * len(words)

        #early exit condition
        if len(s) < window_len:
            return []

        # a hashmap to count the appearance of every words
        word_count = Counter(words)
        ans = []

        #gives different starting location based on the word length.
        for offset in range(word_len):
            l = offset
            seen = Counter()

            #a inner loop to go over the lists starting with different posistions based on the outer loop
            for r in range(offset, len(s) - word_len + 1, word_len):
                #gets the first word in the list
                word = s[r: r + word_len]
                # if the word is not in the target dictionary, then clear the current seen dictionary and increment l
                if word not in word_count:
                    seen.clear()
                    l = r + word_len
                    continue
                #adds the word count to the seen dictionary
                seen[word] += 1
                # a while loop removingt duplicates
                while seen[word] > word_count[word]:
                    #gets the left word
                    left_word = s[l: l + word_len]
                    #decrement the frequency for that word
                    seen[left_word] -= 1
                    #increment l so that the window moves
                    l += word_len
                #if the length of the r which is the start of the last work + the length of the word
                # is equal to the window_len then you can add i
                if r + word_len - l == window_len:
                    ans.append(l)
        
        return ans