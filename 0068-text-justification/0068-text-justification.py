class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            #checks if the current word can fit into the line. 
            # length + length of the word, length of the spaces: length of spaces = len(line) 3 word = 2 spces
            # this is just check so with 2 words adding one word the num of spaces needed would be the length of the original line
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                # Line complete
                #calculates the spaces needed, the reminder is for greedy when it doesn't divide evenly. 
                # the max is used so that lines with 1 word would still work
                extra_space = maxWidth - length
                remainder = extra_space % max(1, (len(line) - 1))
                space = extra_space // max(1, (len(line) - 1))
                # loop to add the lines
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0
    
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res