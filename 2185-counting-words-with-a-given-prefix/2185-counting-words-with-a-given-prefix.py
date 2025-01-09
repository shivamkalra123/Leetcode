class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for x in words:
            if x.startswith(pref)==True:
                c+=1
        return c

        