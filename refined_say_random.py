import random
from subprocess import call

import time

timeout = time.time() + 3 # 3 seconds from now
sip_list = []
puf_list = []
d = {(0, 3): 'yes', (3, 0): 'no', (2, 1): 'maybe', (1, 2): 'certainly not'}

while True:
    test = 0
    ana_val = random.randint(1,30)
    time.sleep(1)
    print (ana_val)
    if ana_val >= 15:
        sip_list.append(ana_val)
    if ana_val < 15:
        puf_list.append(ana_val)

    if test == 3 or time.time() > timeout:
        break
    test = test - 1
# print(sip_list)
# print(puf_list)
print (len(sip_list), len(puf_list))
sp =  (len(sip_list), len(puf_list))

#this one line evals sp(which is the length of the sip/puf lists) it finds the key in the d dict, then it returns the value, which then is put into the say command
call(["say", (d.get(sp))])
