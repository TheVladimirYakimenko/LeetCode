class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_nums = sorted(counter, reverse=True, key=lambda x: counter[x])
        k = min(len(counter), k)
        return sorted_nums[:k]