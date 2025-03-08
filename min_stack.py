# Neetcode solution
class MinStack:
    # T O(1) and M O(n)
    def __init__(self):
        # The strategy is to use two stacks instead of one
        # The first stack is just the regular array stack
        # The second stack is a min stack
        # This means that every index/element/n in min_stack corresponds to 
        # the current minimum element in stack[0:n]
        # So, min_stack holds a list of minimum values of stack where the last
        # element will hold the actual minimum of stack.
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Finding out the "new" current minimum of array
        # with val added into stack
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        # Append current minimum to min stack
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# All I can do is a linked or array implementation of stack so far
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, val: int) -> None:
        if not self.min_element or val < self.min_element:
            self.min_element = val
        self.stack.append(val)

    def pop(self) -> None:
        popped_element = self.stack.pop()
        if popped_element == self.min_element:
            self.min_element = float('inf')
            for ele in self.stack:
                if ele < self.min_element:
                    self.min_element = ele

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element
"""
"""
class MinStack:

    def __init__(self):
        self._heap = []

    def push(self, val: int) -> None:
        self._heap.append(val)
        self._perc_up(len(self._heap) - 1)

    def pop(self) -> None:
        self._heap[0], self._heap[-1] = (
            self._heap[-1],
            self._heap[0]
        )
        self._heap.pop()
        self._perc_down(0)

    def top(self) -> int:
        return self._heap[0]

    def getMin(self) -> int:
        return self._heap[0]

    def _perc_up(self, i):
        # While heap parent exists
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            # If the new val is smaller than its parent
            if self._heap[i] < self._heap[parent_idx]:
                # Let's perform the actual perc up
                # make it switch with its parent
                self._heap[i], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[i]
                )
            i = parent_idx
    
    def _perc_down(self, i):
        while (2 * i + 1) < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = (
                    self._heap[sm_child],
                    self._heap[i]
                )
            else:
                break
            i = sm_child
    
    def _get_min_child(self, i):
        # We are just comparing the left and right child here
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2*i+2]:
            return 2*i+1
        return 2*i+2
"""
"""
class MinStack:

    def __init__(self):

    def push(self, val: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def getMin(self) -> int:

"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()