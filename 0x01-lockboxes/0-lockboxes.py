#!/usr/bin/python3
"""lockbox problem where each box may contain keys to the other boxes"""

def canUnlockAll(boxes):
    visited_boxes = set()

    current_box = 0
    visited_boxes.add(current_box)

    for box in boxes:
        for key in box:
            if key not in visited_boxes:
                visited_boxes.add(key)
                current_box = key
                break
    return len(visited_boxes) == len(boxes)
