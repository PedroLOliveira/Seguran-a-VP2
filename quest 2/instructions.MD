# As instruções abaixo foram todas realizadas em um sistema Windows, porém, serve também para sistemas baseados em UNIX (Linux ou MacOS).

&nbsp;

## Passo 1

- Instalar openssl (biblioteca que iremos usar para gerar as chaves).

```text
sudo apt-get install openssl
```

- Caso utilize sistema Windows, siga os passos descritos no site a seguir: 
    #### [Instalar openssl no windows](https://thesecmaster.com/procedure-to-install-openssl-on-the-windows-platform/)

## Passo 2

- Gerar chave privada RSA de 2048 bits.

```text
openssl genpkey -algorithm RSA -out rsa_private.pem -pkeyopt rsa_keygen_bits:2048
```

## Passo 3

- Gerar chave pública a partir da chave privada gerada no passo anterior.

```text
openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem
```

&nbsp;

- **genpkey**: Informa que será gerada uma chave privada.
- **-out**: Informa o nome do arquivo de saída, ou seja, a chave a ser gerada.
- **-in**: Informa o nome do arquivo a ser utilizado no caso da geração da chave pública com base na privada.
- **-algorithm**: Informa o algoritmo a ser utilizado na geração da chave.
- **-pkeyopt**: Informa o tamanho da chave a ser gerada.
