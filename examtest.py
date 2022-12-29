# s1='Hello world'
# temp=s1[::-1]
# print(temp)

# sli=s1.split()
# sli.reverse()
# str=""
# for i in sli:
#     str=str+" "+i
# print(sli)
# print(str)

# str='      anubhab      sanket       debasish'
# temp=str.split()
# print(temp)
# print(len(temp))
# slr=""
# for i in temp:
#     slr=slr+i.capitalize()+" "
# print(slr)
#
# l1=list(slr)
# print(l1)

# -----------------------------------------------------------------------------------
##Armstrong Number
# a=int(input('Enter the number: '))
# l1=[]
# str=str(a)
# for i in str:
#     l1.append(int(i))
#
# print(l1)
# sum=0
# for i in l1:
#     sum=sum+i**len(l1)
# print(sum)
# if sum==a:
#     print('the number is armstrong')
# else:
#     print('gand marao')


# ---------------------------------------------------------------------------------

# reversing a number
# a=int(input('enter the number: '))
# str=str(a)
# str=str[::-1]
# print('the reversed number is: {}'.format(str))


# def gcd(a,b):
#     if a==0:
#         return b
#     else:
#         return gcd(b%a,a)
#
# def lcm(a,b):
#     return (a*b)/gcd(a,b)

# binary conversion
# a=10
# temp=bin(a)
# print(temp)

# lst=[1,2,3,4,5]
# result=map(lambda a:a**3,lst)
# print(result)

# a={1,2,3,4,5}
# s=tuple(a)
# l1=[2,5,8,9]
# a.add(6)
# s.update(l1)
# print(a)
# print(s)
# s='abcd'
# l=[]
# for i in s:
#     l.append(i)
#
# l.reverse()
# s=''
# for i in l:
#     s=s+i
# print(s)

for i in range(1,6):
    for j in range(i,5):
        print(end='\t')
    for k in range(i,0,-1):
        print(k,end='\t')
    for l in range(2,i+1):
        print(l,end='\t')
    print()

