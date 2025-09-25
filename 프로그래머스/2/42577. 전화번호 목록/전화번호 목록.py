def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        current = phone_book[i]
        next_val = phone_book[i+1]
        if next_val.startswith(current):
            return False
    return True
        