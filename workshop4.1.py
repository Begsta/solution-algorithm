from collections import deque


def length_of_LIS(nums):
    if not nums:
        return 0
        
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)



def update_matrix(mat):
    if not mat or not mat[0]:
        return []

    rows, cols = len(mat), len(mat[0])
    queue = deque()
    dist = [[float('inf')] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))
                
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
    return dist



def run_tests():
    
    assert length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18, 1]) == 4
    assert length_of_LIS([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_LIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert length_of_LIS([1, 2, 3, 4, 5]) == 5

   
    mat1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert update_matrix(mat1) == expected1
    
    mat2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expected2 = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert update_matrix(mat2) == expected2
    print("Все тесты пройдены")

run_tests()
