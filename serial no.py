import keyboard as kb
import time
# Get two numbers from the user
num1 = int(input("Starting serial number: "))
num3 = int(input("How many rolls: "))
num2 = num1+num3
# Find the smaller and larger number
start = min(num1, num2)
end = max(num1, num2)
time.sleep(3)
# Print numbers from small to big
#print("Numbers from", start, "to", end, ":")
for i in range(start, end):
    kb.write(str(i))
    kb.press_and_release('down')
    time.sleep(0.3)
