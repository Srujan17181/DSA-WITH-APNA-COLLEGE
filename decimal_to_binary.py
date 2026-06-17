def decimal_to_binary(decNum):
    ans=0
    pow=1

    while(decNum > 0):
        rem=decNum%2
        decNum=decNum//2
        ans+=rem*pow
        pow*=10

    return ans



print(decimal_to_binary(6))
