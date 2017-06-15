import threading

import time


def thread_job():
        # print("Hello World,the number of this thread is  %s"%threading.current_thread())
        print("T1 start\n")
        for i in range(10):
            time.sleep(0.1)
        print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

def main():
    #创建一个名为"T1",功能为thread_job的线程
    added_thread = threading.Thread(target = thread_job,name="T1")
    thread2 = threading.Thread(target=T2_job,name = 'T2')
    #开始执行added_thread
    added_thread.start()
    thread2.start()
    #强制等待added_thread执行完成后再执行该语句下的内容
    thread2.join()
    added_thread.join()
    print("all done\n")
    # 统计当前处于active状态的线程
    print(threading.active_count())
    #查看active线程名
    print(threading.enumerate())
    #查看运行程序的当前线程
    print(threading.current_thread())


if __name__ == "__main__":
    main()