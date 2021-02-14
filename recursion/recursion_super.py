def move(f, t):
    print("Move disk from {} to {}".format(f,t))

def moveVia(f,v,t):
    move(f,v)
    move(v,t)

def hanoi(n, f, h, t):
    '''

    :param n: Number of disks
    :param f: From position
    :param h: Helper position
    :param t: To position
    :return:
    '''
    if n == 0:
        pass
    else:
        hanoi(n-1, f ,t, h)
        move(f,t)
        hanoi(n-1, h, f, t)


hanoi(4, 'A', 'B', 'C')