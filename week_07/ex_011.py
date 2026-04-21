nums = [20, 36, 27, 15, 2, 107, 48, 66]
no1 = nums[0]

for i in nums:
    if no1 < i:
        no1 = i
        print(f"擂台主換人!新的 no1 = {no1}")

print(f"\n最後冠軍:{no1}")