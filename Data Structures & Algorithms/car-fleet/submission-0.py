class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # for lifo manner
        pairs = [(p,s) for p,s in zip(position, speed)] # store the position and speed using zip
        pairs.sort(reverse=True) # sort in descending as more will be pos, closer to target, lesser the time
        for p,s in pairs:
            stack.append((target - p)/s) # time = distance/speed
            if len(stack)>=2 and stack[-1] <= stack[-2]: # if previous cars speed more, make it a fleet
                stack.pop() # merging the cars
        return len(stack) # the car fleets left in stack is the answer 