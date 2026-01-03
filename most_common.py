from collections import Counter
import re

data = ""
print("enter data (exit to exit) : ")
try :
  while (line := input()) != "exit" :
      data += line + "\n"
except EOFError:
  pass

print(data)

# data = data.replace('/','-').strip()
# data = data.replace(' ','-').strip()
data = re.sub(r'[^\d\n]+','-',data)
data = data.splitlines()

print(data)

for idx in range(0,6) :
    col = list(map(lambda x: x.split('-')[idx], data))
    print(Counter(col).most_common(1))

