import rsa

def encryptMessage(text, key):
    return rsa.encrypt(text.encode(), key)

def decryptMessage(encryptedText, key):
    try:
        return rsa.decrypt(encryptedText, key).decode()
    except:
        return 0

def loadKeys():
    file = open("rsa_private.pem", "rb")
    privateKey = rsa.PrivateKey.load_pkcs1(file.read())
    file.close()

    file = open("rsa_public.pem", "rb")
    publicKey = rsa.PublicKey.load_pkcs1(file.read())
    file.close()

    return publicKey, privateKey

def generateKeys():
    publicKey, privateKey = rsa.newkeys(1024)

    file = open("rsa_private.pem", "wb")
    file.write(privateKey.save_pkcs1('PEM'))
    file.close()

    file = open("rsa_public.pem", "wb")
    file.write(publicKey.save_pkcs1("PEM"))
    file.close()




generateKeys()

publicKey, privateKey = loadKeys()
message = "question 1 from network security"
textEncrypted = encryptMessage(message, publicKey)
textDecrypted = decryptMessage(textEncrypted, privateKey)

print("")
print("Mensagem enviada:", message)
print("")
print("Mensagem criptografada:", textEncrypted)
print("")


if textDecrypted != 0:
    print("Mensagem descriptografada:", textDecrypted)
else:
    print("Erro ao descriptografar a mensagem.")
