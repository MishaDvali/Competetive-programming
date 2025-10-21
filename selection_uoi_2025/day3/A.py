k, n = list(map(int, input().split()))
words = [[] for _ in range(150)]
counter_w = [0 for _ in range(150)]
for _ in range(k):
    word = input()
    words[ord(word[0])].append(word)
for i in range(150):
    words[i].sort()

letters = [input() for _ in range(n)]
for letter in letters:
    ord_letter = ord(letter)
    print(words[ord_letter][counter_w[ord_letter]%len(words[ord_letter])])
    counter_w[ord_letter]+=1


