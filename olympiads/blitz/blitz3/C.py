t = int(input())
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
def check_if_ss(s, i, j, unique):
    letters_met = [0 for _ in range(26)]
    for c in range(i, j+1):
        letters_met[ord(s[c])-97]=1
    amount_of_unique = sum(letters_met)
    return  amount_of_unique >= unique

    

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    s = input()
    n = len(s)
    if k > 26 + 2:
        print("NO")
        continue
    ans_i = None
    ans_j = None
    ans_l = 99999
    letters_indexes = [[] for _ in range(26)]
    for i in range(n):
        letters_indexes[ord(s[i])-97].append(i)
    for letter_indexes in letters_indexes:
        if len(letter_indexes) < 2:
            continue 
        for a in range(0, len(letter_indexes)-1):
            for b in range(a+1, len(letter_indexes)):
                i = letter_indexes[a]
                j = letter_indexes[b]
                if j - i < k + 1:
                    continue
                if j - i >= ans_l:
                    continue
                is_lock = check_if_ss(s, i+1, j-1, k - 2)
                if is_lock:
                    ans_i = i 
                    ans_j = j
                    ans_l = j - i  
    if ans_l == 99999:
        print("NO")   
    else:
        print("YES")
        print(ans_i+1, ans_j+1)              
        
        
