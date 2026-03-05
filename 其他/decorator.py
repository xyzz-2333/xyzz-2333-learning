import time
def decorator1(func):
    def wrapper():
        print("在函数执行前做点什么")
        func()
        print("在函数执行后做点什么")
    return wrapper
@decorator1
def say_hello():
    print("Hello!world!")
def decorator2(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return wrapper
def timedecorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 运行时间: {elapsed:.6f} 秒")
        print(f"运行结果: {result}")
        return result
    return wrapper
@timedecorator
def sleep(time):
    time.sleep(time)
if __name__ == '__main__':
    
    say_hello()
    sleep(0.5)