from collections import deque

d = deque()

d.append(10)        
d.appendleft(20)   
d.append(30)

print("Deque:", d)  

d.pop()            
d.popleft()         

print("After removals:", d)  