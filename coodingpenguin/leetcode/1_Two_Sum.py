# 시간/공간: O(N^2) / O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 모든 요소에 대해서
        for i in range(len(nums)):
            # i번째 요소보다 큰 값들 중
            for j in range(i + 1, len(nums)):
                # i번째 요소의 합이 target과 같다면
                if nums[i] + nums[j] == target:
                    return [i, j]


# 시간/공간: O(N) / O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = {}  # 숫자의 인덱스 저장
        for idx, num in enumerate(nums):
            remained = target - num  # 나머지 숫자
            # 나머지 숫자가 기록되어 있다면 인덱스 쌍 반환
            if remained in num2idx:
                return [num2idx[remained], idx]
            # 그렇지 않다면 인덱스 기록
            else:
                num2idx[num] = idx
