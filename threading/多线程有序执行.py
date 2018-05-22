# —*-coding:utf-8-*-
# 多个线程有序执行
from threading import Thread, Lock
from time import sleep


# 创建锁1 默认没有上锁
lock1 = Lock()
# 创建锁2 并上锁
lock2 = Lock()
lock2.acquire()
# 创建锁3 并上锁
lock3 = Lock()
lock3.acquire()
class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('task1')
                sleep(0.5)
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('task2')
                sleep(0.5)
                lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('task3')
                sleep(0.5)
                lock1.release()



# 创建线程
t1 = Task1()
t2 = Task2()
t3 = Task3()

# 启动线程
t1.start()
t2.start()
t3.start()
