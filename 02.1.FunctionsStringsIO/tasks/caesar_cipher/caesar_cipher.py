def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    lk = []
    fk = []
    for i in range(len(message)):
        if message[i].isupper():
            lk.append(1)
            fk.append(message[i].lower())
        else:
            lk.append(0)
            fk.append(message[i])

    message_ans = ''
    n = n % 26
    for i in range(len(fk)):
        if fk[i].isalpha():
            if ord(fk[i]) + n > 122:
                Buk = chr(96 + (-122 + ord(fk[i]) + n))
            elif ord(fk[i]) + n <= 90 and n < 0:
                Buk = chr(122 - (91 - (ord(fk[i]) + n)))
            else:
                Buk = chr(ord(fk[i]) + n)

            if lk[i]:
                Buk = Buk.upper()

            message_ans += Buk
        else:
            message_ans += fk[i]

    return message_ans


#print(caesar_encrypt('Hello, Arthur', 52))
