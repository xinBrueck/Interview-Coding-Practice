##This function is to sample a large stream with uniform distribution
##the stream is too large to fit in memory,
##so we can't just process everything in the stream and sample element from 0 though size-1

##instead for uniform sampling, we just need to ensure that
##item i, has 1/i chance get sampled(swap the old item that get sampled before item i got processed)
##********This solution is provided by DAILY CODING PRACTICE*****
import random

def uniform_sampling(streamArray):
    random_sample = None
    for i, e in enumerate(streamArray):
        if random.randint(1, i+1) == 1:
            random_sample = e
    return random_sample

##test
streamArray1 = [2]
print(uniform_sampling(streamArray1))
streamArray1 = [2,5]
print(uniform_sampling(streamArray1))
streamArray1 = [2,5,1]
print(uniform_sampling(streamArray1))
streamArray1 = [2,5,1,8]
print(uniform_sampling(streamArray1))
streamArray1 = [2,5,1,8,3]
print(uniform_sampling(streamArray1))
streamArray1 = [2,5,1,8,3,1]
print(uniform_sampling(streamArray1))
