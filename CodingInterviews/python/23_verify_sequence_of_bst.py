#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False

        root = sequence.pop()
        idx = None  # save right node
        for i in range(len(sequence)):
            if idx is None and root < sequence[i]:
                idx = i
            if idx is not None and sequence[i] < root:
                return False
        if sequence[:idx] == []:
            left = True
        else:
            left = self.VerifySquenceOfBST(sequence[:idx])
        if sequence[idx:] == []:
            right = True
        else:
            right = self.VerifySquenceOfBST(sequence[idx:])
        return left and right


if __name__ == "__main__":
    """
          4
        /   \
      2      6
     / \    / \
    1   3  5   7
    """
    # sequence = [1, 3, 2, 5, 7, 6, 4]

    """
      1
       \
        2
    """
    sequence = [2, 1]

    s = Solution()
    ans = s.VerifySquenceOfBST(sequence)
    print(ans)
