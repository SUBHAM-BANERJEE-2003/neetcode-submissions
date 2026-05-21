class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i              # start from i as from there only we will start looking for 
                               # the number that corresponds to the length
            while s[j] != '#': # go till the delimiter which indicates the start of the word
                j += 1
            length = int(s[i : j]) # length can we multiple characters long, like "12"
            word = s[j+1 :j + length + 1] # hash's location to j + length + 1
            ans.append(word)
            i = j + length + 1 # move i to the next numbers location and scan for the next length
        return ans



