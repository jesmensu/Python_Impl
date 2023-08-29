from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from time import sleep
values = [2,3,4,5]
def square(n):
   sleep(3)
   return n * n
def main():
    with ThreadPoolExecutor(max_workers = 3) as executor:
      results = executor.map(square, values)
    for result in results:
      print(result)
if __name__ == '__main__':
   main()