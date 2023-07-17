class Solution:


    @staticmethod
    def Count_of_smaller_Numbers(array):
        res=[]
        for i in range(len(array)):
            c=0
            for j in range(i+1,len(array)):
                if array[i]>array[j]:
                    c+=1
            res.append(c)
        return res

"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

"""


if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(Solution().Count_of_smaller_Numbers(array))