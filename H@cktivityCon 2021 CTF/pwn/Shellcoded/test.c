#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    char v3;
    int i;
    ssize_t v7;
    char *buf = malloc(20);
    v7 = read(0, buf, 4096);
    for ( i = 0; v7 > i; ++i )
    {
      if ( (i & 1) != 0 )
        v3 = -1;
      else
        v3 = 1;
      *((char *)buf + i) += v3 * i;
    }
    int j = 0;
    size_t x = strlen(buf);
    printf("size: %lu\n", x);
    for (; j<x; j++){
        printf("%x-", buf[j]);
    }
    return 0;
}