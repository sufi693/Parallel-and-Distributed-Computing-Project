import multiprocessing
from do_something import do_something

def function_square(data):
    results = []
    do_something(2, results)
    return data * data

if __name__ == '__main__':
    inputs = list(range(10))
    with multiprocessing.Pool(processes=4) as pool:
        outputs = pool.map(function_square, inputs)
    print('Pool:', outputs)
