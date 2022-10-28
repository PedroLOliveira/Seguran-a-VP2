import rsa

def loadPrivateKey(keyPath):
    file = open(keyPath, "rb")
    privateKey = rsa.PrivateKey.load_pkcs1(file.read())
    file.close()

    return privateKey

def signFile(filePath, privKey):
    file = open(filePath, "rb")
    readedFile = file.read()

    signature = rsa.sign(readedFile, privKey, "SHA-256")
    fileName = file.name.split('.')[0]
    
    fileSigned = open(f"{fileName}_assinado.txt", "w")
    fileSigned.writelines([readedFile.decode("utf-8"), signature.hex()])
    fileSigned.close()

    file.close()




while True:
    print("**Assinatura Digital**")
    print("")
    print("1 - Assinar arquivo")
    print("0 - Sair")
    value = int(input("Escolha a opção desejada: "))

    if value == 1:
        filePath = input("Informe a rota do arquivo a ser assinado: ")
        privateKeyPath = input("Informe a rota da chave privada: ")
        privateKey = loadPrivateKey(privateKeyPath)
        signFile(filePath, privateKey)

        print("")
        print("Arquivo assinado!")
        print("")

    elif value == 0:
        break
