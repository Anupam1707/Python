def pwd(string, key):
    key = list(key) 
    if len(string) == len(key):
        return(key) 
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
        return("" . join(key)) 
  
def encrypt(string,password):
    string = string.upper() + " "
    key = pwd(string, password)
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i].upper())) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    encrypt_text = ("" . join(encrypt_text)).upper()
    key = ("".join(key)).upper()
    return encrypt_text + key

def decrypt(encrypt_text):
    orig_text = []
    encrypt_text = encrypt_text.upper()
    b = int(len(encrypt_text)/2)
    key = encrypt_text[b:]
    encrypt_text = encrypt_text[:b-1]
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i].upper()) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    orig_text = ("" . join(orig_text)).upper()
    return orig_text