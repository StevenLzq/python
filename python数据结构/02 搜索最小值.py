#最小值下标
'''


def minofindex(list):
    mindex=0
    curindex=1
    while curindex<len(list):
        if list[curindex] < list[mindex]:
            mindex=curindex
        curindex +=1
    return mindex
a=[443,5,67,878,7,5,45,7,6,8,978,7,3]
print(minofindex(a))

print(a.index(min(a)))


'''

###顺序搜索
'''

def sequentialSearch(target,mylist):
    order=[]
    for i ,j in enumerate(mylist):
        if target==j:
            order.append(i)
    return order



a=[2,3,4,5,6,3,2,3,3]
print(sequentialSearch(3,a))

'''

#有序列表二叉搜索
'''

def binarySearch(target, list):
    left=0
    right=len(list)-1
    while left <=right:
        mid=(left+right)//2
        if target==list[mid]:
            return mid
        elif target<list[mid]:
            right=mid
        else:
            left=mid

    return -1

a=[2,3,4,5,6,7,8]
print(binarySearch(5,a))
'''


def binarySearch(target, list):
    left = 0
    right = len(list) - 1
    memo = {"left": [], 'right': []}
    while left <= right:
        mid = (left + right) // 2
        if target == list[mid]:
            left_num = list[left]
            right_num = list[right]
            memo['left'].append(left_num)
            memo['right'].append(right_num)
            return memo
        elif target < list[mid]:
            left_num=list[left]
            right_num=list[right]

            memo['left'].append(left_num)
            memo['right'].append(right_num)
            right = mid
        else:
            left_num = list[left]
            right_num = list[right]

            memo['left'].append(left_num)
            memo['right'].append(right_num)
            left = mid

    return 0


a = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
print(binarySearch(44, a))




