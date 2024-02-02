import time


def set_time():
    print("Enter the time you'd like to wake up in 24 hour format: ")
    wtime = input()
    return wtime


def clock():
    while True:
        local_time = time.strftime('%H:%M:%S')
        print(local_time)
        alarm(local_time, wtime)
        time.sleep(1)
        if local_time == wtime:
            break


def alarm(local_time, wtime):
    if local_time == wtime:
        print("Wakey wakey")


if __name__ == "__main__":
    wtime = set_time()
    
    try:
        clock()
    except KeyboardInterrupt:
        print("\nClock stopped")