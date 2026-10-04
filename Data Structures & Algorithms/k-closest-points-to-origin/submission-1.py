class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            squared = (x**2) + (y**2)
            heapq.heappush(heap, (-squared, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x,y] for dist, x, y in heap]
        
