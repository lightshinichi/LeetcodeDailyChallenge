#31apr24
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            print(xor)
        # Step 2: Find a bit that is set in the xor result
        diff_bit = xor & (-xor)
       
        # Step 3: Partition the array and find the two unique numbers
        a, b = 0, 0
        for num in nums:
            if num & diff_bit:
                a ^= num
                
            else:
                b ^= num
                

        return [a, b]