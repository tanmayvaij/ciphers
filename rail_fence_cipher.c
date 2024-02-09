#include <stdio.h>
#include <string.h>

void encrypt(char *plainString, int key)
{

    char matrix[key][strlen(plainString)];
    int sign = 1;
    int j = 0;

    for (int i = 0; i < key; i++)
        for (int j = 0; j < strlen(plainString); j++)
            matrix[i][j] = '\0';

    for (int i = 0; i < strlen(plainString); i++)
    {
        matrix[j][i] = plainString[i];

        if (j == key - 1)
            sign = -1;
        else if (j == 0)
            sign = 1;
        j += sign;
    }

    int index = 0;
    for (int i = 0; i < key; i++)
        for (int j = 0; j < strlen(plainString); j++)
            if (matrix[i][j] != '\0')
                plainString[index++] = matrix[i][j];
}

int main()
{

    char plainString[] = "GeeksForGeeks";
    int key = 3;

    encrypt(plainString, key);

    printf("%s", plainString);

    return 0;
}
