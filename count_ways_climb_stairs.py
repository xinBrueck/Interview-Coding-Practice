##This problem is to count the possible ways of climing stairs, also print out each steps took in different ways!
##n_stairs: number of stairs to start climb
##steps: an array of number of steps can take each climb
##counts: count the ways of climbing stairs
##steps_string: start as empty string, append the steps took each time

##I have used recussions
##for each x in steps, I will check whether can take the steps or not
##if can, then take the step and call the function again with n_stairs = n_stairs - steps just took

##finally, when n_stairs == 0, I increment counts to count it as 1 way to climb the stairs
def ways_clim_stairs(n_stairs, steps, counts, steps_string):
    if n_stairs == 0:
        counts += 1
        print(steps_string)
        return counts
    else:
        for x in steps:
            if x <= n_stairs: ##check whether can take x steps
                #print("n_stairs = {}, steps = {}".format(n_stairs, x))
                counts = ways_clim_stairs(n_stairs - x, steps, counts, steps_string+str(x)+",")
    return counts


##tests:
steps = [1, 2]
n_stairs = 4
counts = 0
steps_string = ""
print("possibles ways to climb the stairs when there are 4 stairs total, can take 1 or 2 each steps")
count1 = ways_clim_stairs(n_stairs, steps, counts, steps_string)
print("Total number of ways: {}".format(count1))


##tests:
steps = [1, 3, 5]
n_stairs = 4
counts = 0
steps_string = ""
print("possibles ways to climb the stairs when there are 4 stairs total, can take 1 or 3 or 5 each steps")
count2 = ways_clim_stairs(n_stairs, steps, counts, steps_string)
print("Total number of ways: {}".format(count2))
