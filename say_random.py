import random
from subprocess import call

import time

timeout = time.time() + 3 # 3 seconds from now
sip_list = []
puf_list = []

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
sp1 = (0, 3)
sp2 = (1, 2)
sp3 = (2, 1)
sp4 = (3, 0)

if sp == sp1:
    print('yes')
    call(["say", "yes"])
if sp == sp2:
    print('no')
    call(["say", "no"])
if sp == sp3:
    print('maybe')
    call(["say", "maybe"])
if sp == sp4:
    print('certainly not')
    call(["say", "certainly not"])
