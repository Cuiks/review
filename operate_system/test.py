# -*- coding: utf-8 -*-
import time

from operate_system import pool, task


class SimpleTask(task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)


def process():
    time.sleep(1)
    print("This is a Simple Task callable function.1")
    time.sleep(1)
    print("This is a Simple Task callable function.2")


def test():
    # 1、初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2、生成一系列任务
    for i in range(10):
        simple_task = SimpleTask(process)
        # 3、往线程池提交任务执行
        test_pool.put(simple_task)


def test_async_task():
    def async_process():
        num = 1
        for i in range(100):
            num += i
        return num

    # 1、初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2、生成一系列任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        # 3、往线程池提交任务执行
        test_pool.put(async_task)
        result = async_task.get_result()
        print(f"get result: {result}")


# 测试是否可以真正的等待(wait)
def test_async_task2():
    def async_process():
        num = 1
        for i in range(100):
            num += i
        time.sleep(1)
        return num

    # 1、初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2、生成一系列任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        # 3、往线程池提交任务执行
        test_pool.put(async_task)
        print(f"get result in timestamp: {time.time()}")
        result = async_task.get_result()
        print(f"get result in timestamp: {time.time()}, result: {result}")


# 测试没有等待是否也可以正常获取结果
def test_async_task3():
    def async_process():
        num = 1
        for i in range(100):
            num += i
        return num

    # 1、初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2、生成一系列任务
    for i in range(1):
        async_task = task.AsyncTask(func=async_process)
        # 3、往线程池提交任务执行
        test_pool.put(async_task)
        print(f"get result in timestamp: {time.time()}")
        time.sleep(5)
        result = async_task.get_result()
        print(f"get result in timestamp: {time.time()}, result: {result}")


if __name__ == '__main__':
    # test()
    test_async_task()
