
def two_sum(numbers,target,ans):
    left=0
    right=len(numbers) - 1
    print(left)
    print(right)
    while left<right:
        if numbers[left] + numbers[right] == target:
            return left,right
        elif numbers[left] + numbers[right] > target:
            right = right - 1
        else:
            left = left + 1
numbers = [2,7,11,15]
target = 22
ans=[]
ans = two_sum(numbers,target,ans)
print(f'The indexs ares: {ans}')
        