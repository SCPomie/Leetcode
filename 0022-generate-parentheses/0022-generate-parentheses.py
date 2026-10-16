class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #initialise the result list and variables
        ans = []
        open_used = 0
        close_used = 0
        prefix = ""

        #start backtracking
        self.generate_par(prefix, n, open_used, close_used, ans)

        return ans

    def generate_par(self, prefix, n, open_used, close_used, ans):
        #base case if all n pairs are used
        if open_used == n and close_used == n:
            ans.append(prefix)
            return

        #add an opening bracket if we haven't used all n
        if open_used < n:
            self.generate_par(prefix + "(", n, open_used + 1, close_used, ans)

        #add a closing bracket if there are unmatched opening brackets
        if close_used < open_used:
            self.generate_par(prefix + ")", n, open_used, close_used + 1, ans)