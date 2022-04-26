#Upal has found Florians password hash, he wants to crack it. Upal knows that Florian has an obsession with a specific star wars character, but cant remember which, can you help Upal hack his colleague?
#Upal has told you that Florian is obsessed with 1337 speak, so  "1 th1nk y0u m4y n33d s0m3 CUST0M RUL3S"
#Submit the flag as TDCNET{PASSWORD_HERE}
# `$2b$12$VFXRbeO68bfKwBHXscm2G.cctp8d9hRKdmOCjb9t3fVQgFv4YKfjK`
# 
# https://en.wikipedia.org/wiki/List_of_Star_Wars_characters#Dressellians we take "Orrimaarko"
import bcrypt
import time
name,name1337 = b"Orrimaarko", b"0rr1m44rk0"

start = time.time()
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(name1337,salt)
end = time.time()

print(end-start)
print(hashed)