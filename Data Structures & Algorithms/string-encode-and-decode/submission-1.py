class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            size = len(s)
            res.append(str(size) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #.  5#Hello6#Worldd
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            start = j + 1
            end = start + size
            res.append(s[start:end])
            i = end
        
        return res


