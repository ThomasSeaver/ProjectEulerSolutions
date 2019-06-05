# feel like there should be a better approach but 100% solved

# pre-calculate fibonacci numbers, and cache our result whenever we get to a
# longer number. This way we can pre-calculate all possible test cases,
# which is more efficient since worst case is calculating all tests anyway
fibonacci_lengths = [0, 1]
max_length = 1
f_a = 1
f_b = 1
pos = 2

while max_length <= 5000:
    curr = f_a + f_b
    pos += 1
    if len(str(curr)) > max_length:
        fibonacci_lengths.append(pos)
        max_length += 1
    f_a = f_b
    f_b = curr

t = int(input())
for _ in range(t):
    n = int(input())
    print(fibonacci_lengths[n])