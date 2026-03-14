nums = [1, 1, 2,2,4,4, 3, 3, 3]
# k=0
# j=1
# for i in range(len(nums)-1):
#     # for j in range(i+1,len(nums)-1):
#     if nums[i]==nums[j]:
#         print(f'i={i}')
#         print(f'j={j}')
#         j+=1
#     else:
#         k+=1
#         print(f'i={i}')
#         print(f'j={j}')
#         print(f'k={k}')
#         nums[k]=nums[j]
#         print(nums)
#         j+=1
# print(nums)




# Array sorted hota hai.

# Do pointer use karte hain → i aur j.

# i = last unique element ka index.

# j = next element check karega.

# i = 0 se start karo.

# j = 1 se loop chalao end tak.

# Agar nums[i] == nums[j] → duplicate → skip.

# Agar nums[i] != nums[j] → new element mila.

# i = i + 1 karo.

# nums[i] = nums[j] store karo.

# Loop ke baad unique elements ki length = i + 1.


def remove_duplicate(nums):
    i=0
    for j in range(0,len(nums)):
        if nums[i] !=nums[j]:
            i=i+1
            nums[i]=nums[j]
    print(nums)
    return i+1
nums= [1,1,1,1,2,2,3,4,4,5,5,0]
k=remove_duplicate(nums)
print(f'VaLUE OF K IS {k}')


def remove_duplicates_using_brute_force(nums):

    n = len(nums)

    for i in range(n-1):

        if nums[i] == nums[i+1]:

            # left shift
            for j in range(i+1, n-1):
                nums[j] = nums[j+1]

            n -= 1

    return n


nums = [1, 1, 2,2, 3, 3, 3]

k = remove_duplicates_using_brute_force(nums)

print(f'using brute force approch :{k}')
print(nums)



