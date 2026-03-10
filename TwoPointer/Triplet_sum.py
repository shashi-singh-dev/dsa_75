# def triplet(num,target):
#     # ans=[]
#     for i in range(len(num)-1):
#         l=i+1
#         r=len(num)-1
#         while(l<r):
#             # print(i,l,r) this is to understand the loop flow
#             if num[i]+num[l]+num[r] == target:
#                 print(num[i],num[l],num[r],num[i]+num[l]+num[r])
#                 ans.append([num[i],num[l],num[r]])
#                 l+=1
#                 r-=1
#             elif num[i]+num[l]+num[r] < target:
#                 l+=1
#             elif num[i]+num[l]+num[r] > target:
#                 r-=1
#     return ans

# num = [-3,-2,-1,0,1,2,3]
# num.sort()
# target = 0
# ans=[]
# ans=triplet(num,target)
# print(ans)

num = [-3,-2,-1,0,1,2,3]
target = 0
ans=[]
n=len(num)
for i in range(n):
    # print(i)
    for j in range(i+1,n):
        # print(j)
        for k in range(j+1,n):
            if num[i]+num[j]+num[k]== target:
                ans.append([num[i],num[j],num[k]])
                ans.sort()
print(ans)