class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}|{s}'
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != '|':
                j += 1
            
            lenofs = int(s[i:j])
            start = j+1
            end = start + lenofs

            result.append(''.join(s[start:end]))
            
            i = end
        return result
        



