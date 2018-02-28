import time
from inspect import stack

__all__=["timeFunc"]

def timeFunc(func):
    def t(*args,**kwargs):
        st = time.time()
        x = func(*args,**kwargs)
        et = round((time.time() - st)*1000)
        print(stack()[1][3],'called',func.__name__,'and executed in',et,'ms')
        return x
    return t

def runTest():
    @timeFunc
    def test():
        print("Hello world")

    test()
    

if __name__=='__main__':
    runTest()
