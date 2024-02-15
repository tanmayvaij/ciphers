// Caesar Cipher Code

#include <stdio.h>
#include <string.h>

void encrypt(char *plainText, int key)
{
    for (int i = 0; i < strlen(plainText); i++)
    {
        if (plainText[i] >= 65 && plainText[i] <= 91)
            plainText[i] = ((plainText[i] - 65 + key) % 26) + 65;

        else if (plainText[i] >= 97 && plainText[i] <= 123)
            plainText[i] = ((plainText[i] - 97 + key) % 26) + 97;
    }
}

void decrypt(char *cipherText, int key)
{
    for (int i = 0; i < strlen(cipherText); i++)
    {
        if (cipherText[i] >= 65 && cipherText[i] <= 91)
            cipherText[i] = ((cipherText[i] - 65 - key + 26) % 26) + 65;

        else if (cipherText[i] >= 97 && cipherText[i] <= 123)
            cipherText[i] = ((cipherText[i] - 97 - key + 26) % 26) + 97;
    }
}

int main()
{
    char text[] = "tanmayvaij";
    int key = 5;

    encrypt(text, key);

    printf("encryted text: %s \n", text);

    decrypt(text, key);

    printf("decrypted text: %s \n", text);

    return 0;
}
