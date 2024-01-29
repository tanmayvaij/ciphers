#include <stdio.h>
#include <string.h>

void encrypt(char *plainString, int n)
{
    for (int i = 0; i < strlen(plainString); i++)
    {
        if (plainString[i] >= 65 && plainString[i] <= 91)
        {
            plainString[i] = ((plainString[i] - 65 + n) % 26) + 65;
        }
        else if (plainString[i] >= 97 && plainString[i] <= 123)
        {
            plainString[i] = ((plainString[i] - 97 + n) % 26) + 97;
        }
    }
}

void main()
{
    char plainString[] = "abcdefghijklmnopqrstuvwxyz";
    encrypt(plainString, 5);
    printf("%s", plainString);
}
