from collections import deque

# Create deque
d = deque()

# Insert elements
d.append(10)        # Insert at rear
d.appendleft(20)    # Insert at front
d.append(30)

print("Deque:", d)  # Deque([20, 10, 30])

# Remove elements
d.pop()             # Remove from rear → 30
d.popleft()         # Remove from front → 20

print("After removals:", d)  # Deque([10])
