class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return s.search(".*".join(list(s)),t)