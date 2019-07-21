##This problem is to count the possible ways of climing stairs
##n_stairs: number of stairs to start climb
##steps: an array of number of steps can take each climb
##counts: count the ways of climbing stairs

##I have used recussions
##for each x in steps, I will check whether can take the steps or not
##if can, then take the step and call the function again with n_stairs = n_stairs - steps just took

##finally, when n_stairs == 0, I increment counts to count it as 1 way to climb the stairs
def ways_clim_stairs(n_stairs, steps, counts):
    if n_stairs == 0:
        counts += 1
        return counts
    else:
        for x in steps:
            if x <= n_stairs: ##check whether can take x steps
                print("n_stairs = {}, steps = {}".format(n_stairs, x))
                counts = ways_clim_stairs(n_stairs - x, steps, counts)
    return counts


##tests:
steps = [1, 2]
n_stairs = 4
counts = 0

print(ways_clim_stairs(n_stairs, steps, counts))


##tests:
steps = [1, 3, 5]
n_stairs = 4
counts = 0

print(ways_clim_stairs(n_stairs, steps, counts))
