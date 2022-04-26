#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <signal.h>
#include <seccomp.h>
#include <seccomp-syscalls.h>

#define MAXSIZE 1024

void setup_bufs() {
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void sig_handler(int signum) {
    exit(-1);
}

static int install_seccomp(void) {
    scmp_filter_ctx ctx;
    // Default allow, cause we don't want to break anything
    ctx = seccomp_init(SCMP_ACT_ALLOW);

    // Blacklist
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(fork), 0);
    
    seccomp_load(ctx);

}

int main() {
    void (*func)(void);
    setup_bufs();
    
    signal(SIGALRM, sig_handler);
    //alarm(10);
    char *code = mmap(NULL, MAXSIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    ssize_t r = read(STDIN_FILENO, code, MAXSIZE-1);
    for (int i = 0; i < r; i++) {
        if (code[i] == 0) {
            printf("Illegal byte\n");
            exit(-1);
        }
    }
    func = (void*)code;
    install_seccomp();
    func();
}