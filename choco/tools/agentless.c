#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concat(const char *s1, const char *s2);

int main(int argc, char **argv)
{
    char *arr=malloc(1000*sizeof(char));
    int i;
    for(i = 0; i < argc - 1; i++){
        arr = concat(concat(arr, " "), argv[i+1]);
    }

	system(concat("python.exe -c \"exec(\\\"from agentless import *;laucher()\\\")\" ", arr));
}

char* concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}
