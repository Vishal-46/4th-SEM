#include <stdio.h>
#include <string.h>
#include <stdlib.h>

main(int argc, char *argv[])
{
    FILE *fd;
    char str[100];
    char c;
    int i, k, m;
    char temp[30];
    
    if (argc != 3)
    {
        printf("Usage: gcc mygrep.c -o mygrep\n");
        printf("Usage: ./mygrep <search_text> <filename>\n");
        exit(-1);
    }
    
    fd = fopen(argv[2], "r");
    if (fd == NULL)
    {
        printf("%s does not exist\n", argv[2]);
        exit(-1);
    }
    
    while (!feof(fd))
    {
        i = 0;
        while (1)
        {
            c = fgetc(fd);
            if (feof(fd))
            {
                str[i] = '\0';
                break;
            }
            if (c == '\n')
            {
                str[i] = '\0';
                break;
            }
            str[i++] = c;
        }
        
        if (strlen(str) >= strlen(argv[1]))
        {
            for (k = 0; k <= strlen(str) - strlen(argv[1]); k++)
            {
                for (m = 0; m < strlen(argv[1]); m++)
                    temp[m] = str[k + m];
                temp[m] = '\0';
                
                if (strcmp(temp, argv[1]) == 0)
                {
                    printf("%s\n", str);
                    break;
                }
            }
        }
    }
}