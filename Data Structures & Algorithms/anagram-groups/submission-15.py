class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            arraydef = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                arraydef[idx] = arraydef[idx] + 1
            
            arraytup = tuple(arraydef)
            hashmap[arraytup].append(word)
        
        res = []

        for item in hashmap.values():
            res.append(item)

        return res