class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        curr_best = strs[0][:min_len]

        for i in range(1, len(strs)):
            match_up_to = 0

            while match_up_to < len(curr_best):
                if curr_best[match_up_to] == strs[i][match_up_to]:
                    match_up_to += 1
                else:
                    curr_best = curr_best[:match_up_to]
                    break

        return curr_best