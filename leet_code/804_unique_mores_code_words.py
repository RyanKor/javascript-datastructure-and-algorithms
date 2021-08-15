# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        answer = []
        for i in words:
            temp = list(i)
            for j in range(len(temp)):
                temp[j] = morse[alphabet.index(temp[j])]
            answer.append(''.join(temp))
        return len(set(answer))