def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    '''
    Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'
    Step 1: Shift first disk from 'A' to 'B'
    Step 2: Shift second disk from 'A' to 'C'
    Step 3: Shift first disk from 'B' to 'C'
    Pattern:
    Shift 'n-1' disks from 'A' to 'B'
    Shift last disk from 'A' to 'C'
    Shift 'n-1' disks from 'B' to 'C'
    '''
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

# driver
n = 4
tower_of_hanoi(n, 'A', 'C', 'B')
# A,C, B are the name of the rods