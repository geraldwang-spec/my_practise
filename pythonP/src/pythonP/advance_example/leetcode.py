

from unittest import result


class Solution:
    def runningSum(self, nums:list[int]) -> list[int]:
        total_tmp:int = 0
        length:int = len(nums)
        result: list[int] = [0] * length
        for i in range(0, length):
            total_tmp += nums[i]
            result[i] = total_tmp

        return result

    def maximumWealth(self, accounts: list[list[int]])->int:
        max: int = 0
        temp: int = 0
        for sublist in accounts:
            temp = 0
            for item in sublist:
                temp += item
            if temp > max:
                max = temp

        return max

    def maximumWealth_test(self, accounts: list[list[int]])->int:
        max_wealth: int = 0
        for sublist in accounts:
            sublist_wealth: int = sum(sublist)
            if sublist_wealth > max_wealth:
                max_wealth = sublist_wealth
        return max_wealth

    def maximumWealth_test1(self, accounts: list[list[int]])->int:
        return max(sum(person) for person in accounts)

    def fizzBuzz(self, n :int) -> list[str]:
        result:list[str] = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                result.append("Fizz")
            elif i % 3 != 0 and i%5 == 0:
                result.append("Buzz")
            else :
                result.append(str(i))
        return result
 
    def fizzBuzz_test1(self, n :int) -> list[str]:
        result:list[str] = []
        for i in range(1, n+1):
            s:str = ""
            if i%3 == 0: s += "Fizz"
            if i%5 == 0: s += "Buzz"
            if i%7 == 0: s += "Jazz"
            result.append(s if s else str(i))
        return result
    
    def fizzBuzz_advence(self, matrix: list[list[int]]) -> list[list[str]]:
        result:list[list[str]] = []
        for sublist in matrix:
            row:list[str] = []
            for item in sublist:
                s:str = ""
                if item%3 == 0: s += "Fizz"
                if item%5 == 0: s += "Buzz"
                if item%7 == 0: s += "Jazz"
                row.append(s if s else str(item))
            result.append(row)
   
        return result

def leetCode_basic()->None:
    ss:Solution = Solution()
    # print(f"result =  {ss.runningSum([1,2,3,4])}")
    # print(f"maximumWealth result = {ss.maximumWealth([[2,8,7],[7,1,3],[1,9,5] ])}")
    # print(f"maximumWealth_test result = {ss.maximumWealth_test([[2,8,7],[7,1,3],[1,9,5] ])}")
    # print(f"maximumWealth_test1 result = {ss.maximumWealth_test1([[2,8,7],[7,1,3],[1,9,5] ])}")
    # print(f"fizzBuzz result = {ss.fizzBuzz(27)}")
    # print(f"fizzBuzz_test1 result = {ss.fizzBuzz_test1(27)}")
    print(f"fizzBuzz_advence result = {ss.fizzBuzz_advence([[2,8,27],[7,15,3],[21,9,5] ])}")

def leetCode_test()->None:
    print(f"leetCode_test")
    leetCode_basic()
