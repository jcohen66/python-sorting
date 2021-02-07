from queue import PriorityQueue

pq = PriorityQueue()
pq.put(1)
pq.put(2)
pq.put(3)

print(pq.get())
print(pq.get())
print(pq.get())

pq.put(3)
pq.put(2)
pq.put(1)

print(pq.get())
print(pq.get())
print(pq.get())

pq.put(3)
pq.put(-1)
pq.put(-5)

print(pq.get())
print(pq.get())
print(pq.get())

pq.put((1, "hello"))
pq.put((2, "world"))

print(pq.get())
print(pq.get())

print(pq.empty())