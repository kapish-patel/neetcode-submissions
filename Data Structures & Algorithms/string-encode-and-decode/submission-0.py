class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"{length}|{s}"
        return res
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        lengthofs = len(s)
        while i < lengthofs:

            j=i
            while s[j] != '|':
                j+=1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length
            result.append(''.join(s[start:end]))

            if i > lengthofs:
                return result

            i = end

        return result
