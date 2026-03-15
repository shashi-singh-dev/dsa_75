# def check_plndrm(string,l,r):  
#     print(f'l={l} & r={r}') 
#     while l<r:
       
#         if string[l] != string[r]: 
#             return False
#         l=l+1
#         r=r-1
#     return True
# def palindrome(string):
#     l=0
#     r=len(string)-1
#     while l<r:
#         if string[l]!=string[r]:
#             print("calling")
#             return check_plndrm(string,l+1,r) or check_plndrm(string,l,r-1)
#         else:
#             l=l+1
#             r=r-1 
#     return True   

# string='abSSDDba'
# v=palindrome(string)
# print(f'value of v is : {v}')


s = "abcDa"

for i in range(len(s)):

    new_string = ""

    for j in range(len(s)):
        if j != i:
            new_string += s[j]
    if new_string == new_string[::-1]:
                print(f'{new_string} is palindrome')
    else:
          print(f'{new_string} is not palindrome')
 

