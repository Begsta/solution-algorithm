from collections import deque
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)

    return heap[0]


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def main():
    assert level_order(None) == []

    root_single = TreeNode(1)
    assert level_order(root_single) == [[1]]

    root_standard = TreeNode(3)
    root_standard.left = TreeNode(9)
    root_standard.right = TreeNode(20)
    root_standard.right.left = TreeNode(15)
    root_standard.right.right = TreeNode(7)
    assert level_order(root_standard) == [[3], [9, 20], [15, 7]]

    root_lefty = TreeNode(1)
    root_lefty.left = TreeNode(2)
    root_lefty.left.left = TreeNode(3)

    assert level_order(root_lefty) == [[1], [2], [3]]

    print("Первые тесты пройдены!")

    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    assert find_kth_largest([1], 1) == 1

    assert find_kth_largest([-1, -1], 2) == -1

    assert find_kth_largest([7, 6, 5, 4, 3, 2, 1], 5) == 3

    print("Тесты пройдены!")


if __name__ == "__main__":
    main()
