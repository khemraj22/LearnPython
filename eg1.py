# Write script to sum of all digits of a given number. For example if the number is 487, the output should be 19.

number = 487
total = 0

while(number>0):
        rem=number%10
        total += rem
        number=number/10

print total


n = "1423"
t = 0
for c in n:
    t += int(c)
    
print t
