from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        window_len = word_len * len(words)


        if len(s) < window_len:
            return []
        
        word_count = Counter(words)
        ans = []

        for offset in range(word_len):
            l = offset
            seen = Counter()

            for r in range(offset, len(s) - word_len + 1, word_len):
                word = s[r: r + word_len]
                if word not in word_count:
                    seen.clear()
                    l = r + word_len
                    continue
                seen[word] += 1
                while seen[word] > word_count[word]:
                    left_word = s[l: l + word_len]

                    seen[left_word] -= 1
                    l += word_len
                
                if r + word_len - l == window_len:
                    ans.append(l)
        
        return ans