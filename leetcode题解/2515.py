class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        r=-1
        if target not in words:
            return -1
        idx=[i for i, x in enumerate(words) if x == target]
        for i in idx:

            tmp=min(abs(i-startIndex),len(words)-abs(i-startIndex))
            if r==-1 or tmp <r:
                r=tmp

        return r