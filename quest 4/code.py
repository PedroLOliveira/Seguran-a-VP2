
import rsa

def loadPublicKey(keyPath):
    file = open(keyPath, "rb")
    publicKey = rsa.PublicKey.load_pkcs1(file.read())
    file.close()

    return publicKey

def verifyAuthenticity(filePath, publicKey, sign):
    file = open(filePath, "rb")
    
    try:
        content = file.read()[:-256]
        file.close()

        return rsa.verify(content, sign, publicKey) == "SHA-256"

    except:
        file.close()

        return 0




while True:
    print("**Assinatura Digital**")
    print("")
    print("1 - Validar assinatura")
    print("0 - Sair")
    value = int(input("Escolha a opção desejada: "))

    if value == 1:
        signedFilePath = input("Informe a rota do arquivo a ser validado: ")
        publicKeyPath = input("Informe a rota da chave pública: ")
        publicKey = loadPublicKey(publicKeyPath)
        sign = open(signedFilePath, 'r').read()[-256:]
        signBytes = bytes.fromhex(sign)
        result = verifyAuthenticity(signedFilePath, publicKey, signBytes)

        if result != 0:
            print("")
            print("Assinatura validada")
            print("")
        else:
            print("")
            print("Assinatura inválida")
            print("")

    elif value == 0:
        break
