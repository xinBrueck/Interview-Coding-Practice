#This function is to check whether the sum of any 2 elements in the list
#equals to n
def sum_to_n(list, n):
  for i in range(len(list)):
    for j in range(i+1,len(list)):
      if (list[i] + list[j] == n):
          return True
  return False

test_list = [0, -1, 20, 9, 200, 4.3, 400]
n1 = 20
n2 = -3

print(sum_to_n(test_list, n1))
print(sum_to_n(test_list, n2))
