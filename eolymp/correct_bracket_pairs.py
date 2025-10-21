def amount_of_variants(sequence: str, balance: int) -> int:
    if len(sequence) == 0:
        if balance == 0:
            return 1
        return 0
    if sequence[-1] == "(":
        return amount_of_variants(sequence[:-1], balance - 1)
    if sequence[-1] == ")":
        return amount_of_variants(sequence[:-1], balance + 1)
    if balance < 0:
        return 0
    if len(sequence) < balance:
        return 0
    if len(sequence) == balance:
        return 1
    return amount_of_variants(sequence[:-1], balance - 1) + amount_of_variants(sequence[:-1], balance + 1)


def main():
    sequence = input()
    if len(sequence) % 2 == 1:
        return 0
    return amount_of_variants(sequence, 0)

if __name__ == "__main__":
    while True:
        print(main())
