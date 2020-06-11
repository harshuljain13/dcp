"""
Given the string with A and B characters, get the maximum perfectness of the 
string by changing no more than k characters. A string is perfect if it has 
all the characters same. example: aaaaa, bbbbb
"""

def get_maximum_perfectness(s,k,c):
    l = 0
    r = 0
    cnt=0
    res = 0
    while r<len(s):
        if s[r]!=c:
            cnt+=1
        while cnt>k:
            if s[l] != c:
                cnt-=1
            l+=1
        res = max(res, r-l+1)
        r+=1
    return res

print(max(get_maximum_perfectness('AAABA', 1, 'A'), get_maximum_perfectness('ABAB', 1, 'B')))