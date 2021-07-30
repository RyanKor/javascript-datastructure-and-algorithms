# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0
        d = {}

        for letter in chars:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        for word in words:
            present = True
            for letter in word:
                if (letter not in d) or (d[letter] < word.count(letter)):
                    present = False
                    break
            if present:
                s += len(word)

        return s