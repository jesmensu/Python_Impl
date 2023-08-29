import multiprocessing

global_value = 0.0
def calc_square(numbers, result, v):
    global global_value
    v.value = 5.67
    global_value = v.value*2
    for idx, n in enumerate(numbers):
        result[idx] = n*n

    print("global_value in process ", global_value)

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(v.value)
    print(result[:])
    print("global_value in main ", global_value)