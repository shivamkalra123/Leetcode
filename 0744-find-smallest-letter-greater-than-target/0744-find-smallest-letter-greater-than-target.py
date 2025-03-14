from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(set(letters))  

        for i in range(len(letters)):
            if ord(letters[i]) == ord(target):
                if i == len(letters) - 1:
                    return letters[0]
                else:
                    return letters[i + 1]
            if ord(letters[-1]) < ord(target):
                return letters[0]
            if ord(letters[i]) > ord(target):
                return letters[i]
