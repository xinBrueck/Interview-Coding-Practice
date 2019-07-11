#This function accepts a list and return a list
#each ith element in the result list is the product of the original list without the ith element

##############logic to solve the problem
#if there is more than one 0, the result_list would just be all populated with 0
#if there is only one 0, only the ith place in the result_list that corresponds to the 0 in the list would have nonzero result_list
#if there is no 0, for version1: the ith place in the result_list the product of the list divided by the ith value in the original list
#if there is no 0, for version2: the ith place in the result_list should be multiple left product and right product of the ith number
#keep track of the left_product and right_product when iterate through each i
#################

from functools import reduce

def product_exclude_i_v1(li):
    ##count the number of zeros in the list
    zero_flag_list = list(map((lambda x: int(x==0)), li))
    zero_counts = sum(zero_flag_list)

    result_list = [0]*len(li)
    if zero_counts > 1:
        return result_list
    elif zero_counts == 1:
        #get the index of zero
        index_zero = li.index(0)
        #remove zero from the original list for multiplication
        li.remove(0)
        result_list[index_zero] = reduce((lambda x, y: x*y), li)
        return result_list
    elif zero_counts == 0:
        result_list = []
        list_prod = reduce((lambda x, y: x*y), li)
        for x in li:
            result_list.append(list_prod/x)
        return result_list



def product_exclude_i_v2(li):

    ##count the number of zeros in the list
    zero_flag_list = list(map((lambda x: int(x==0)), li))
    zero_counts = sum(zero_flag_list)

    result_list = [0]*len(li)
    if zero_counts > 1:
        return result_list
    elif zero_counts == 1:
        #get the index of zero
        index_zero = li.index(0)
        #remove zero from the original list for multiplication
        li.remove(0)
        result_list[index_zero] = reduce((lambda x, y: x*y), li)
        return result_list
    elif zero_counts == 0:
        result_list = []
        left_product = 1
        right_product = reduce((lambda x, y: x*y), li)

        for x in li:
            right_product /= x
            result = left_product * right_product
            result_list.append(result)
            left_product *= x


        return result_list

list_test1 = [-1, 2, 3, 4, 5]
list_test2 = [1,0,0,2]
list_test3 = [1,1,0,2]

print(product_exclude_i_v1(list_test1))
print([120, -60, -40, -30, -24])
print(product_exclude_i_v1(list_test2))
print([0,0,0,0])
print(product_exclude_i_v1(list_test3))
print([0,0,2,0])

print(product_exclude_i_v2(list_test1))
print([120, -60, -40, -30, -24])
print(product_exclude_i_v2(list_test2))
print([0,0,0,0])
print(product_exclude_i_v2(list_test3))
print([0,0,2,0])
