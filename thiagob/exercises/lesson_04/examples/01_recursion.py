import time

def count_down_r(n):
    # check to define when to stop
    if n < 0:
        return

    # execution to call it again
    print(n)
    time.sleep(1)
    count_down_r(n-1)

def count_down_i(n):
    for n in range(n,-1,-1):
        print(n)
        time.sleep(1)


count_down_r(5)
count_down_i(5)