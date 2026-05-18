def length_of_LIS(nums):
    if not nums:
        return 0
        
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)


def main():
  
    assert length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18, 1]) == 4,
    
    assert length_of_LIS([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_LIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert length_of_LIS([1, 2, 3, 4, 5]) == 5
    
    print("Тесты пройдены")


main()
