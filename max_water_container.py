def brute_force_Max_water(hgt):
    max_area = 0
    for i in range(len(hgt)):
        for j in range(i+1,len(hgt)):
            area= min(hgt[i],hgt[j]) * (j - i)
            # print(f'hgt[i]={hgt[i]} & hgt[j]={hgt[j]} & area is:{area}) & {i},{j}')
            max_area=max(max_area,area)
    return(max_area)
    

def Max_water(hgt):
    max_area=0
    l=0
    r=len(hgt)-1
    max_area = 0
    while l<r:
        area= min(hgt[l],hgt[r]) * (r - l) 
        max_area = max(max_area,area)
        if hgt[l]<hgt[r]:
            l=l+1
        else:
            r=r-1
    return(max_area)

hgt=[1,8,6,2,5,4,8,3,7]
print(f'maximum water area using brute force approach is :{brute_force_Max_water(hgt)}')
print(f'maximum water area is using two pointer approach is :{Max_water(hgt)}')

#time complexity using brute force : O(n²)
#time complexity using two pointer : O(n)
#space complexity = O(1)

        