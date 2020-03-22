def fillNum(nums):
    tmp = [nums[0]]*len(nums)
    flag = True
    while flag:
        flag = False
        for i,j in enumerate(nums):
            if tmp.count(j) != tmp[i]:
                flag = True
                tmp[i] = tmp.count(j)
    return tmp

print(fillNum([0,1,2,3,4,5,6,7,8,9]))