text = input("Enter a sentence:") or "I love learning pyhton"

print("Length=",len(text))
print("Characters in the given text:")
for ch in text:
    print(ch,end =",")