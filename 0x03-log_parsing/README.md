# Log parsing

## Read stdin line by line:

- Use a loop to read input lines from stdin until a keyboard interruption (CTRL + C) or end of input.
- Parse each line to extract relevant information, specifically the IP Address, date, request details, status code, and file size.
- Skip lines that do not match the specified format.


## Compute metrics:

- Maintain a counter for the total file size. Add the file size from each valid line to this counter.
- Maintain a dictionary to count the number of lines for each status code (200, 301, 400, 401, 403, 404, 405, 500).
- Print statistics after every 10 lines or keyboard interruption:

## Keep track of the line count.

If the line count reaches 10 or a keyboard interruption occurs, print the following statistics:

- Total file size: File size: <total size>
- Number of lines by status code in ascending order.


## Handle exceptions:

- Catch exceptions related to keyboard interruptions to ensure a graceful exit.


## Repeat the process until the end of input:

- Continue reading lines and computing metrics until the end of input.
