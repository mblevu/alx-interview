from collections import deque
#!/usr/bin/python3
"""lockbox problem where each box may contain keys to the other boxes"""

def canUnlockAll(boxes) -> bool:
    visited_boxes = set()
    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()
        visited_boxes.add(current_box)

        for key in boxes[current_box]:
            if key not in visited_boxes:
                queue.append(key)

    return len(visited_boxes) == len(boxes)
