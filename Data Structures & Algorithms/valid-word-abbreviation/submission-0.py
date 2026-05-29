class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer into word
        j = 0  # pointer into abbr

        while i < len(word) and j < len(abbr):

            # Case 1: current abbreviation character is a letter
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

            # Case 2: current abbreviation character is a digit
            else:
                # Leading zeros are invalid
                if abbr[j] == '0':
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

                # Skipped beyond the end of the word
                if i > len(word):
                    return False

        return i == len(word) and j == len(abbr)