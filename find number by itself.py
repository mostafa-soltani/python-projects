save = 0
save2 = 0
import random
num_rnd = random.randint(1,20000)
num_rnd2 = random.randint(1,20000)
save = num_rnd
save2 = num_rnd2
print(num_rnd2,num_rnd)
while num_rnd != num_rnd2:
    
    if num_rnd2 < num_rnd : 
        num_rnd2 = random.randint(save,20000)
        print(num_rnd,num_rnd2)
        save = num_rnd2

    elif num_rnd2 > num_rnd : 
        num_rnd2 = random.randint(1,save)
        print(num_rnd,num_rnd2)
        save = num_rnd2



print('i found it 0001101101111010101010011100100011010111000010010001')

