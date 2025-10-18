def move_zeros_to_end(arr):
    n = len(arr)
    pos = 0  # Position to place the next non-zero element

    # First pass: move non-zero elements forward
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    # Second pass: fill remaining positions with zeros
    for i in range(pos, n):
        arr[i] = 0

    return arr  # Optional: for easy testing
