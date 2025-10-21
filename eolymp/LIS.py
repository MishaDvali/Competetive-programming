import bisect

def patience_sort(cards):
    n = len(cards)
    decs = [] 
    pred = [None] * n 
    card_to_index = {} 

    for i, card in enumerate(cards):
        pos = bisect.bisect_left([stack[-1] for stack in decs], card)
        if pos == len(decs):
            decs.append([card])
        else:
            decs[pos].append(card)
        if pos > 0:
            pred[i] = decs[pos-1][-1]
        card_to_index[card] = i
    lis = []
    current = decs[-1][-1] 
    while current is not None:
        lis.append(current)
        current_index = card_to_index[current]
        current = pred[current_index]
    
    return lis[::-1] 

cards = list(map(int, input().split()))
print(patience_sort(cards))

