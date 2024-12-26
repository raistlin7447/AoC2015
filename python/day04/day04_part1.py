from hashlib import md5

secret_key = open("day04_input.txt").read()

answer = 0
while True:
    test = secret_key + str(answer)
    result = md5(test.encode()).hexdigest()
    if result[:5] == "00000":
        break
    answer += 1

print(answer)