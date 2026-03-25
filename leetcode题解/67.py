class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a))+bin(int(b)))[2:]