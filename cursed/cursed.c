// gcc -m32 cursed.c -fno-stack-protector -o docker/cursed
#include <stdio.h>
#include <unistd.h>
void setup_bufs() {
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}
void win() {
    char *v[] = {"/bin/sh", NULL};
    char *e[] = {NULL};
    execve("/bin/sh", v, e);
}
void vuln() {
    char c[110];
    gets(c);
}
int main() {
    setup_bufs();
    vuln();
    return 0;
}