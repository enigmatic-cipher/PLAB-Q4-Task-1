"""
Given a string as input. Create a new string in which every occurrence of character 'd' is doubled.
Input-> "code"
Output-> "codde"
"""

st = "code"
ln = len(st)
st1 = ""
for i in range(0,ln):
  ch = st[i]
  if(ch=="d"):
    st1 = st + ch + "d"
print(st1)

