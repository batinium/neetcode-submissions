class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)

        for c in strs:
            sets["".join(sorted(c))].append(c)
        
        return list(sets.values())