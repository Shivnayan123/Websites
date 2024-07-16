# def intTostr(i):
#     digits = '0123456789'
#     if i==0:
#         return '0'
#         result =''

#         while i>0:
#             result=digits[i%10]+result
#             i=i%10
#             return result

# a=[1,2,3,4]
# b=[2,3,4,5,6]

# for i in a:
#     for j in b:
#         if i<j:
#             print('({},{})'.format(i,j))

# a=[1,2,3,4]
# b=[2,3,4,5,]

# for i in a:
#     for j in b:
#         for k in range(100000):
        
#             print('({},{})'.format(i,j))

# L=[1,2,3,4,5]

# for i in range(0,len(L)//2):
#     other = len (L)-i-1
#     temp =L[i]
#     L [i]=L[other]
#     L[other]=temp
#     print(L)

# def power (num):
#     if num<1:
#         return 0
#     elif num == 1:
#             print(1)
#             return 1
#     else:
#         prev = power (num//2)
#     curr =prev*2
#     print(curr)
#     return (curr)
#     power(10)
#     print(power)

# def sum_digit(num):
#     sum =0
#     while (num>0):
#         sum +=num%10
#         num/=10
#         return sum