    def twoSum(nums, target):
        nums = nums
        target = target
        output = []

        for i in range(len(nums)):
            sub = target - nums[i]
            print("Sub: ",sub)

            if sub in nums and nums.index(sub) != i:
                output.append(i)
                output.append(nums.index(sub))
                break

        return output
        
