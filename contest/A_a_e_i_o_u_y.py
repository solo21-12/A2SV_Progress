n = int(input())
word = input()

vowels = set(['a', 'e', 'i', 'o', 'u','y'])
result = []
l = 0

while l < len(word):
    while l < len(word) and result and word[l] in vowels and result[-1] in vowels:
        l += 1

    if l < len(word):
        result.append(word[l])
        
    l += 1

print("".join(result))
