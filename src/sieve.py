import time

def sieve_of_Eratosthenes(n):
    start_time=time.time()
    is_prime=[True]*(n-1)
    p=2

    while True:
        multiplier=2
        multiple=p*multiplier # (2p,3p,4p,5p,6p,7p)
        
        while multiple<=n:
            is_prime[multiple-2]=False
            multiplier+=1
            multiple=p*multiplier

        for i,prime in enumerate(is_prime):
            if prime and i+2>p:
                p=i+2
                break
        else:
            break

    end_time=time.time()
    for i,prime in enumerate(is_prime):
        if prime: print(i+2)
    print("time: %0.5f"%(end_time-start_time))

sieve_of_Eratosthenes(1000000)