class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for c in strs:
            mydict["".join(sorted(c))] += [c]

        return list(mydict.values())