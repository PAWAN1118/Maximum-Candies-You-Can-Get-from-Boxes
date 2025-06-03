from collections import deque

def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
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

            # Gain new keys and boxes
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
            # We cannot open the box yet, re-queue it for later
            queue.append(box)

    return total_candies
