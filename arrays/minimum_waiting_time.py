def minimum_waiting_time(queries):
    queries.sort()
    ptr = 0
    wait_time = 0
    num_of_queries = len(queries)

    print(queries)
    while(ptr < num_of_queries):
        # All remaining queries must wait this amount of time
        remaining_queries = num_of_queries - ptr - 1
        wait_time += remaining_queries * queries[ptr]
        # Advance the ptr
        ptr += 1

    return wait_time

# Driver
l = [3,2,1,2,6]
print(minimum_waiting_time(l))


