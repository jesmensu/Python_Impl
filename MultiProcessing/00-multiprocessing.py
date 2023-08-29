import time
from multiprocessing import Process

def calc_square(numbers):
    for n in numbers:
        time.sleep(1)
        print('square ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(1)
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [11, 22, 33]
    p1 = Process(target=calc_square, args=(arr1,))
    p2 = Process(target=calc_cube, args=(arr2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")