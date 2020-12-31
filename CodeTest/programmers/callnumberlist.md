```
def solution(phone_book):
    answer = True
    phone_book.sort()
    sortPhoneBook = sorted(phone_book)
    for i in range(0,len(sortPhoneBook)-2):
        if sortPhoneBook[i] in sortPhoneBook[i+1] :
            return False;

    return answer
```