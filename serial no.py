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


#  # Get two numbers from the user
#  num1 = int(input("Enter first number: "))
#  num2 = int(input("Enter second number: "))
#  
#  # Find the smaller and larger number
#  start = min(num1, num2)
#  end = max(num1, num2)
#  
#  # Print numbers from small to big
#  print("Numbers from", start, "to", end, ":")
#  for i in range(start, end + 1):
#      print(i, end=" ")
#  

#  import pyautogui
#  import time
#  
#  # Get two numbers from the user
#  num1 = int(input("Enter first number: "))
#  num2 = int(input("Enter second number: "))
#  
#  # Determine the range
#  start = min(num1, num2)
#  end = max(num1, num2)
#  
#  # Delay to give you time to focus on the typing window (e.g., Notepad)
#  print("Typing will start in 5 seconds... Please open a text field.")
#  time.sleep(5)
#  
#  # Type numbers from start to end
#  for i in range(start, end + 1):
#      pyautogui.typewrite(str(i) + ' ')
#      time.sleep(0.1)  # slight delay between numbers
