class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(lambda:[])
        for x in strs:
            n=" ".join(sorted(x))
            a[n].append(x)
        return list(a.values())
    



   
        
        