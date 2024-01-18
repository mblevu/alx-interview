# Minimum operations

## Problem Statement:

In a text file, you start with a single character 'H'. Your text editor allows two operations: Copy All and Paste. Given a number 'n', you need to find the minimum number of operations required to obtain exactly 'n' 'H' characters in the file.

## Approach:

You have a file with a single 'H' character.
You can perform two operations: Copy All (Ctrl+A) and Paste (Ctrl+V).
These operations allow you to duplicate the existing characters in the file.

### Goal:

The goal is to figure out the minimum number of operations needed to have 'n' 'H' characters in the file.

### Initial State:

Start with one 'H' in the file (the initial state).

### Operations:

Copy All: Copies the existing content of the file.
Paste: Pastes the copied content after the existing content.

### Example:

Let's take an example with n = 9.
Starting with 'H', we can perform operations:
Copy All => Paste => 'HH'
Paste => 'HHH'
Copy All => Paste => 'HHHHHH'
Paste => 'HHHHHHHHH'
Total operations: 6

## General Approach:

Start with one 'H'.
If n is 1, return 0 (as we are already there).
For each i from 2 to n:
If n is divisible by i:
Copy All the content and Paste it (i-1) times.
Continue this process until n is achieved.
Keep track of the minimum number of operations.

## Result:

Return the minimum number of operations.


```
minOperations(9)

Result: 3
```