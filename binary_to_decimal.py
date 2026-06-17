def binary_to_decimal(binNum):
    ans=0
    pow=1
    while(binNum > 0):
        rem=binNum%10
        ans+=rem*pow
        binNum=binNum//10
        pow*=2

    return ans

print(binary_to_decimal(1010))