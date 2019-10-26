# 封装了用户调用tqdm时候的简单操作
from tqdm import tqdm,trange
import time

__author__ = 'Raven'

def tqdm_usercall_raven(rangenum,funtion):
    startnum = 0
    tqdm(ascii=True)
    try:
        with trange(rangenum,ncols=75) as t:
            for startnum in t:
                funtion()
                pass
    except KeyboardInterrupt:
        t.close()
        raise
    t.close()


# tqdm.close()
# for i in range(100):
#     print('\r',end='')
#     for j in range(i):
#         print("*",end='',sep='')
#     time.sleep(0.01)


        