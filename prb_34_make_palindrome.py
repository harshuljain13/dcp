def make_palindrome(s):
    '''
    recursion implementation
    '''
    #base case 1
    if not s or len(s)==1:
        return s

    #base case 2
    if s==s[::-1]:
        return s
    
    if s[0] == s[-1]:
        return s[0]+make_palindrome(s[1:-1]) + s[-1]
    else:
        x = s[0] + make_palindrome(s[1:]) + s[0]
        y = s[-1] + make_palindrome(s[:-1]) + s[-1]

        if len(x)>len(y):
            return y
        elif len(x)<len(y):
            return x
        else:
            return min(x,y)

print(make_palindrome("leetcode"))

