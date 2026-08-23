class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=set(nums)
        arr=[]
        for i in num:
            arr.append(i)
        arr.sort(reverse=True)
        if len(arr)>=3:
            return arr[2]
        else:
            return arr[0]

        print(arr)