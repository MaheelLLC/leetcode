# Also part of my attempt
class MaxHeap:
    def __init__(self):
        self._heap = []
    
    def insert(self, val):
        self._heap.append(val)
        self._perc_up(len(self._heap) - 1)

    def delete(self):
        if not self._heap:
            return 0
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result
        
    def heapify(self, nums):
        self._heap = nums
        idx = len(nums) // 2 - 1

        while idx >= 0:
            self._perc_down(idx)
            idx -= 1
    
    def _perc_down(self, i):
        while (2 * i + 1) < len(self._heap):
            lg_child = self._get_max_child(i)
            if self._heap[i] < self._heap[lg_child]:
                self._heap[i], self._heap[lg_child] = (
                    self._heap[lg_child],
                    self._heap[i]
                )
            else:
                break
            i = lg_child
    
    def _get_max_child(self, i):
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2*i+1] > self._heap[2*i+2]:
            return 2*i+1
        return 2*i+2

    def _perc_up(self, i):
        # while a parent exists
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self._heap[i] > self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[i]
                )
            i = parent_idx

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # turn all of the stones elements into negatives
        stones = [-s for s in stones]
        # convert stones array into a negative min heap 
        # (which is just another way of saying max heap)
        heapq.heapify(stones)
        # while the stones heap still has more than 1 element
        while len(stones) > 1:
            # pop out the first largest stone
            first = heapq.heappop(stones)
            # pop out the second largest stone
            second = heapq.heappop(stones)
            # calculate the difference between both stones (smash them together)
            difference = first - second
            # if the stones were equal in size
            if difference == 0:
                # don't add it back to the stones heap
                continue
            else:
                # we still have a remaining stone, add it back to the heap
                heapq.heappush(stones, difference)
            
        # if the stones heap still has a remaining stone
        if stones:
            return -stones[0]
        # else, we smashed all of the rocks
        else:
            return 0
        # Neetcode solution: We will use a min heap of 
        # negative numbers to simulate a max heap

        # We are multiplying all of the elements in the list
        # by -1, so we can properly use a min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # So since they are all negative, instead of 
            # checking if the first stone is bigger than
            # the second stone, we'll say the opposite.
            # first stone is -y in this case and second
            # stone is -x. 
            if second > first:
                # We want to put the negative difference
                # of the stones into the negative heap
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])



        # My attempt
        heap = MaxHeap()
        heap.heapify(stones)
        while len(heap._heap) > 1:
            stone_1 = heap.delete()
            stone_2 = heap.delete() if heap._heap else 0
            if stone_1 == stone_2:
                continue
            else:
                new_stone = stone_1 - stone_2
                heap.insert(new_stone)
        if heap._heap:
            return heap._heap[0]
        else:
            return 0
            