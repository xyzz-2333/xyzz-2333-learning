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

def timer(func):
    #需要time库
    #第一个有实际意义的装饰器，实测可用
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时 {end-start:.4f} 秒")
        print(f"运行结果: {result}")
        return result
    return wrapper
@timer
def slow_function(t):
    time.sleep(t)
    return "完成"
if __name__ == '__main__':
    slow_function(1)
    #say_hello()
    #sleep(0.5)