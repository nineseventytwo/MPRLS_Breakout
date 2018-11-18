import random
from subprocess import call

import time
# sip_list = []
# puf_list = []
# timeout = time.time() + 3 # 3 seconds from now
d = {(0, 3): 'yes', (3, 0): 'no', (2, 1): 'maybe', (1, 2): 'certainly not'}

def reading_loop():
    try:
        while True:
            t = 3
            sip_list = []
            puf_list = []
            while t > 0:
                ana_val = random.randint(1,30)
                time.sleep(1)
                print (ana_val)
                if ana_val > 15:
                    sip_list.append(ana_val)
                if ana_val < 15:
                    puf_list.append(ana_val)
                if ana_val == 15:
                    pass
                t = t - 1

            print (len(sip_list), len(puf_list))
            sp =  (len(sip_list), len(puf_list))
            word = (d.get(sp))
            
            if word in d.values():
                print(word)
                call(["say", word ])
            else:
                pass
    except KeyboardInterrupt:
        print('exited program')
# print(sip_list)
# print(puf_list)

reading_loop()
# print (len(sip_list), len(puf_list))
# sp =  (len(sip_list), len(puf_list))
# word = (d.get(sp))

# if word in d.values():
#     print(type(word))
#     call(["say", word ])
# else:
#     pass
#this one line evals sp(which is the length of the sip/puf lists) it finds the key in the d dict, then it returns the value, which then is put into the say command
# call(["say", word ])
