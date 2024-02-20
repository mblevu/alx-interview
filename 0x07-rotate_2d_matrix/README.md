# Rotate 2D matrix

## Problem:

Given an n×n 2D matrix, rotate it 90 degrees clockwise. The matrix must be edited in-place.


## Approach:
To rotate the matrix 90 degrees clockwise, we can follow these steps:

 - Transpose the Matrix: Swap the rows and columns of the matrix. This effectively rotates the matrix 90 degrees counterclockwise.
- Reverse Each Row: Reverse each row of the transposed matrix. This completes the clockwise rotation by flipping each row horizontally.