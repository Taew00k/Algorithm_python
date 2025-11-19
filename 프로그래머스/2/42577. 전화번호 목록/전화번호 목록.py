def solution(phone_book):
    phone_book.sort()
    for p in range(1, len(phone_book)):
        if phone_book[p].startswith(phone_book[p-1]):
            return False
    return True