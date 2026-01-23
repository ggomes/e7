def is_prime(n):
    if not isinstance(n,int) or n<=1:
        return False
    for i in range(2,int(1+n/2)):
        if n%i==0:
            return False
    return True