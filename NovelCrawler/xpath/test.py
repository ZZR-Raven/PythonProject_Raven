from tqdm import tqdm,trange
import time

tqdm(ascii=True)
try:
    with trange(100000) as t:
        for i in t:
            # print('hh')
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


        