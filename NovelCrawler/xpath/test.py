# from tqdm import tqdm
import time

# with tqdm(total=100) as pbar:
#     for i in (range(100)):
#         # tqdm.write("wtf")
#         time.sleep(1)
#         pbar.update(1)

# tqdm.close()
for i in range(100):
    print('\r',end='')
    for j in range(i):
        print("*",end='',sep='')
    time.sleep(0.01)

        