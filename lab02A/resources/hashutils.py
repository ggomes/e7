
import hashlib
import numpy as np

def signif(x, p=1):
    if isinstance(x,int) or (isinstance(x,np.ndarray) and x.dtype==int):
        return x
    x = np.asarray(x)
    x_positive = np.where(np.isfinite(x) & (x != 0), np.abs(x), 10**(p-1))
    mags = 10 ** (p - 1 - np.floor(np.log10(x_positive)))
    return np.round(x * mags) / mags

def get_hash(num,sigdig=1):
    if isinstance(num,str):
        return hashlib.md5(num.encode()).hexdigest()
    else:
        return hashlib.md5(str(signif(num, sigdig)).encode()).hexdigest()