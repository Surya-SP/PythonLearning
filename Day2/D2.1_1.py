# Write a program that adds the digits in a 2 digit two_digit_numberber. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_numberber = input("Type a two digit two_digit_numberber: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
sum_of_digits = 0
for digit in str(two_digit_numberber):
    sum_of_digits += int(digit)
print(sum_of_digits)
