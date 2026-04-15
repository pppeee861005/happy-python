MACH_SPEED = 1225
DISTANCE_TO_MOON = 384400

total_hours = DISTANCE_TO_MOON / MACH_SPEED
days = int(total_hours // 24)
hours = int(total_hours % 24)

print("總共需要天數")
print(days)
print("小時數")
print(hours)