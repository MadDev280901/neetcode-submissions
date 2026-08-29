class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        window = [0] * 26
        firstWord = [0] * 26
        
        # Count frequencies of the target string s1
        for ch in s1:
            firstWord[ord(ch) - ord('a')] += 1
            
        # Slide the window over s2
        for i in range(0, len(s2) - len(s1) + 1):
            if i == 0:
                # Initialize the first window
                for j in range(0, len(s1)):
                    window[ord(s2[j]) - ord('a')] += 1
            else:
                # Remove the character left behind
                window[ord(s2[i - 1]) - ord('a')] -= 1
                # Add the new character entering the window
                window[ord(s2[i + len(s1) - 1]) - ord('a')] += 1
            
            if window == firstWord:
                return True
                
        return False