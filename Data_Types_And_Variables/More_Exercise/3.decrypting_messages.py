key = int(input())
n = int(input())
massage = ""

for i in range(n):
    ch = ord(input())
    current_ch = key + int(ch)
    massage == chr(current_ch)

print(massage)