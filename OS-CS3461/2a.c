#include <stdio.h>
#include <dirent.h>

main()
{
    struct dirent **namelist;
    int n, i;
    char pathname[100];
    
    getcwd(pathname, sizeof(pathname));
    n = scandir(pathname, &namelist, 0, alphasort);
    if (n < 0)
        printf("Error\n");
    else
        for (i = 0; i < n; i++)
            if (namelist[i]->d_name[0] != '.')
                printf("%-20s", namelist[i]->d_name);
}