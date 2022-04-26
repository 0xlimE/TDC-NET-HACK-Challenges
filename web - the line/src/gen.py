# Generate the wordlist
# with open("dawikifull.txt","r") as f:
#     with open("dawikishorter.txt","w+") as g:
#         while True:
#             word = f.readline()[:-1]
#             word = word.lower()
#             if len(word) > 5 and len(word) < 10 and "æ" not in word and "ø" not in word and "å" not in word:
#                 g.write(word+"\n")

import random

FLAG = "TDCNET{Spr1ng_0v3r_1_K03n}"
NUM_STEPS = 9521
WAIT_TIME = 10
sitelist = ["index.html"]
with open("dawikishorter.txt","r") as f:
    words = f.read().splitlines()
    for i in range(NUM_STEPS):
        sitelist.append(random.choice(words)+random.choice(words)+random.choice(words)+".html")


def writehtml(first, second, inline):
    with open(first,"w+") as out:
        out.write("""
<!DOCTYPE html>
<html>
   <head>
      <title>Waiting in line</title>
      <meta http-equiv = "refresh" content = "%s; url = ./%s" />
   </head>
   <body>
      <h1>You are number %s in line!</h1>
      <h2>Please be patient wit us!</h2>
   </body>
</html>"""%(str(WAIT_TIME),second,str(inline)))
        

for i in range(NUM_STEPS):
    writehtml(sitelist[i],sitelist[i+1],NUM_STEPS-i)

#Here we write the flag
with open(sitelist[NUM_STEPS],"w+") as out:
        out.write("""
<!DOCTYPE html>
<html>
   <head>
      <title>Thanks for waiting!</title>
   </head>
   <body>
      <h1>You have finished waiting in line!</h1>
      <h2>Thanks for being patient, here is your flag: %s</h2>
   </body>
</html>"""%FLAG)
