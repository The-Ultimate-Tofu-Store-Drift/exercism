def rotate(phrase, n):
    
    plain_key = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain_key[:]
    cipher = list(cipher)

    for i in range(n):
        cipher.append(cipher[0])
        del cipher[0]

    result = []

    for i in range(len(phrase)):

        if phrase[i] == phrase[i].upper() and phrase[i].isalpha():
            result.append(cipher[plain_key.index(phrase[i].lower())].upper())
        
        elif phrase[i].isalpha():
            result.append(cipher[plain_key.index(phrase[i].lower())])
        
        else:
            result.append(phrase[i])
    
    return "".join(result)


if __name__ == "__main__":
    print(rotate(input("phrase: "), int(input("n: "))))
