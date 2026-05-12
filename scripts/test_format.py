from model_inspector import _format_indices

# Single element
assert _format_indices([5]) == "5"

# Two contiguous
assert _format_indices([3, 4]) == "3-4"

# Two with step
assert _format_indices([3, 5]) == "3,5"

# Short contiguous (≤6)
assert _format_indices([0, 1, 2, 3, 4, 5]) == "0-5"

# Long contiguous
assert _format_indices(list(range(0, 43))) == "0-42"

# Short AP (step=2, ≤6 elements)
assert _format_indices([2, 4, 6]) == "2,4,6"
assert _format_indices([2, 4, 6, 8, 10, 12]) == "2,4,6,8,10,12"

# Long AP (step=2, >6 elements)
assert _format_indices([2, 4, 6, 8, 10, 12, 14]) == "2,4,...,12,14"
assert _format_indices(list(range(2, 43, 2))) == "2,4,...,40,42"

# Short AP (step=3)
assert _format_indices([0, 3, 6, 9, 12]) == "0,3,6,9,12"

# Long AP (step=3)
assert _format_indices(list(range(0, 31, 3))) == "0,3,...,27,30"

# Mixed: contiguous prefix [0,1] + AP tail [3,5,...,59]
indices_mixed = [0, 1] + list(range(3, 61, 2))
assert _format_indices(indices_mixed) == "0-1,3,5,...,57,59"

# Mixed: AP prefix [0,2,...,20] (step=2) + contiguous tail [21-25] (step=1)
# Boundary element 20 belongs to the first AP run
indices_mixed2 = list(range(0, 20, 2)) + list(range(20, 26))
assert _format_indices(indices_mixed2) == "0,2,...,16,18,20-25"

# Mixed: two short runs
assert _format_indices([0, 1, 5, 7, 9]) == "0-1,5,7,9"

# Alternating step pattern
assert _format_indices([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == "0,2,...,16,18"
assert _format_indices([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == "1,3,...,17,19"

# Mixed contiguous + step AP
assert _format_indices([0, 1] + list(range(3, 60, 2))) == "0-1,3,5,...,57,59"
assert _format_indices([0, 1, 2] + list(range(3, 60, 2))) == "0-3,5,7,...,57,59"

# Non-AP short (≤6 elements, gaps differ)
assert _format_indices([1, 5, 7, 12]) == "1,5,7,12"

# Mixed: contiguous + isolated element + contiguous
# 10 is isolated (gap 1→8→1), so 3 runs: [0-2], [10], [11-12]
assert _format_indices([0, 1, 2, 10, 11, 12]) == "0-2,10-12"

# Empty list
assert _format_indices([]) == ""

# Full AP step=2 long sequence
assert _format_indices(list(range(0, 100, 2))) == "0,2,...,96,98"

# Two disjoint contiguous ranges
assert _format_indices([0, 1, 2, 100, 101, 102]) == "0-2,100-102"

# Single element repeated (impossible in practice, but defensive)
assert _format_indices([7]) == "7"

# Step=2 ending with isolated element that continues the step
# [2,4,6,8,10] → one step=2 run
assert _format_indices([2, 4, 6, 8, 10]) == "2,4,6,8,10"

# Alternating two patterns interleaved by sig (simulate attn/mlp layers)
# odd indices = shape A, even indices = shape B → each sub-group compresses
# Here just test the raw index formatting for odd/even
assert _format_indices(list(range(1, 60, 2))) == "1,3,...,57,59"
assert _format_indices(list(range(0, 60, 2))) == "0,2,...,56,58"

# Three runs: step=3, then contiguous, then step=2
indices_three = [0, 3, 6, 9, 20, 21, 22, 30, 32]
assert _format_indices(indices_three) == "0,3,6,9,20-22,30,32"

# Long result triggers abbreviation (>40 chars when joined)
indices_long = []
for base in range(0, 200, 20):
    indices_long.extend([base, base + 2, base + 4, base + 6])
result_long = _format_indices(indices_long)
assert result_long == "0,2,4,6,20,22,24,26,40,42,44,46,60,62,64,66,80,82,84,86,100,102,104,106,120,122,124,126,140,142,144,146,160,162,164,166,180,182,184,186"

# Peel boundary: step=2 run + contiguous tail at the seam
# [0,2,4,6,8,10,11,12,13,14] → 0,2,...,8,10-14
indices_peel = [0, 2, 4, 6, 8, 10, 11, 12, 13, 14]
assert _format_indices(indices_peel) == "0,2,4,6,8,10-14"

print("All tests passed!")
