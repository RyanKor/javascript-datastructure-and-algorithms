class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # s[:] = s[:][::-1]

        def recursive(start, end, s):
            if start == len(s) // 2:
                return

            s[start], s[end] = s[end], s[start]
            recursive(start + 1, end - 1, s)

        recursive(0, len(s) - 1, s)
