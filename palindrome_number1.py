def pali(x):
    di_list = [int(dig)  for dig in str(x)]
    i =0
    j = len(di_list)-1
    while i<=j:
        if di_list[i] != di_list[j]:
            return False
        i+=1
        j-=1
    return True



# check = x
# check2 =0
# while(check>0):
#     check2 = check%10 + check2*10
#     check = check/ 10
# return check2 == x


# if x<0: return False
# di_list = [int(dig)  for dig in str(x)]
# if di_list == di_list[::-1]:
#     return True
# else:
#     return False



print(pali(121))