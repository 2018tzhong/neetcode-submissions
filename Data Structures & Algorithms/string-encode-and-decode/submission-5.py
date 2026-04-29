class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_string = ""
        for i in strs:
            encoded_string += i + ";!;"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []
        return s.split(";!;")[:-1]