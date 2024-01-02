# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Counter and heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, cnt in count.items():
            heappush(heap, (-cnt, num))
        
        answer = []
        for _ in range(k):
            answer.append(heappop(heap)[1])
        return answer

# Counter and Sort 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(), key = lambda item:item[1], reverse = True)
        answer = []
        for key, value in count:
            answer.append(key)
            k -= 1
            if k == 0:
                break
        return answer