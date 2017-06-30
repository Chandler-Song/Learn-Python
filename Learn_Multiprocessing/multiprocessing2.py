import Learn_Multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes = 2)
    res = pool.map(job,range(10))
    print(res)
    # res = pool.apply_async(job,(2,2,4,5))
    # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print ([res.get() for res in multi_res])

if __name__ == "__main__":
    multicore()