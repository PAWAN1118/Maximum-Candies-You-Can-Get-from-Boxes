from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        queue = deque(initialBoxes)
        have_keys = set()
        have_boxes = set(initialBoxes)
        visited = set()
        total_candies = 0

        while queue:
            box = queue.popleft()
            if box in visited:
                continue

            if status[box] == 1 or box in have_keys:
                visited.add(box)
                total_candies += candies[box]

                for k in keys[box]:
                    if k not in have_keys:
                        have_keys.add(k)
                        if k in have_boxes and k not in visited:
                            queue.append(k)

                for b in containedBoxes[box]:
                    if b not in have_boxes:
                        have_boxes.add(b)
                    if status[b] == 1 or b in have_keys:
                        queue.append(b)
            else:
                queue.append(box)

        return total_candies
