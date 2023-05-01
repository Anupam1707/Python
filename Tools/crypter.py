def Key(string, key):
    key = list(key) 
    if len(string) == len(key):
        return(key) 
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
        return("" . join(key)) 
  
def encrypt(string,password):
    string = string.upper()
    key = Key(string, password)
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i])) % 26
        x += ord('a')
        encrypt_text.append(chr(x))
    encrypt_text = ("" . join(encrypt_text)).upper()
    key = ("".join(key)).upper()
    return encrypt_text, key

def decrypt(encrypt_text, key):
    orig_text = []
    encrypt_text.upper()
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
        x += ord('a')
        orig_text.append(chr(x))
    orig_text = ("" . join(orig_text)).upper()
    return orig_text
