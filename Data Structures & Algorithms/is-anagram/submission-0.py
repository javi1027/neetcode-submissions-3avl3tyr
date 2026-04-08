class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = "".join(sorted(s))
        nt = "".join(sorted(t))

        return ns == nt

        