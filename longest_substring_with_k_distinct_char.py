##This function takes in 2 parameter:
##a string: origString
##an integer: n_distinct

##to return the longest substring that contains n_distinct number of unique chars
##for example, if input "sdfssa", 3, it will return "sdfss"

def longestSubstring(origString, n_distinct):
    if n_distinct == 0 or len(origString) == 0:
        print("Empty string or Zero distinct char!")
        return ""
    elif (len(set(origString))) <= n_distinct or len(origString) <= n_distinct:
        print("Number of distinct char in {} is smaller than {}".format(origString, n_distinct))
        return origString
    else:
        longestSubstr = origString[0: n_distinct]
        longestSubstrLen = len(longestSubstr)
        startPos = 0
        endPos = n_distinct + 1

        while (startPos < len(origString) - longestSubstrLen) and (endPos < len(origString)):
            tempSubstr = origString[startPos: endPos]
            if len(set(tempSubstr)) <= n_distinct:
                if len(tempSubstr) > longestSubstrLen:
                    longestSubstr = tempSubstr
                    longestSubstrLen = len(tempSubstr)
                endPos += 1
            else:
                startPos += 1
        return longestSubstr

##testing
print("test1")
s1 = "sdfisdyyhhhhh"
k = 4
print(longestSubstring(s1, k))

print("test2")
s2 = "df"
k = 4
print(longestSubstring(s2, k))

print("test3")
s2 = "dddddddddd"
k = 4
print(longestSubstring(s2, k))

print("test4")
s2 = "abcba"
k = 2
print(longestSubstring(s2, k))
