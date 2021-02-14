def towers_of_hanoi(n, source, dest, aux):
    print(f"n {n} source {source} dest {dest} aux {aux}")
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {dest}")
        return

    towers_of_hanoi(n-1, source, aux, dest)
    print(f"Move disk {n} from source {source} to destination {dest}")
    towers_of_hanoi(n-1, aux, dest, source)

# driver
n = 4
towers_of_hanoi(n, 'A', 'B', 'C')