def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("* "*n)
  
# Driver Code
n = 5
pypart(n)