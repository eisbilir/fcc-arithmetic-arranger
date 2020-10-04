import re

def arithmetic_arranger(problems,*exit):
  if len(problems)>5:
    return "Error: Too many problems."

  if any(not bool(re.search("^\w* [+-] \w*$",val)) for val in problems):
    return "Error: Operator must be '+' or '-'."

  if any(bool(re.search("[a-zA-Z]",val)) for val in problems):
    return "Error: Numbers must only contain digits."
  
  if any(bool(re.search("\d{5,}",val)) for val in problems):
    return "Error: Numbers cannot be more than four digits."
  
  s=""
  for val in problems:
    x=re.split(" [+-] ",val)
    s=s+" "*2+" "*(max(len(x[0]),len(x[1]))-len(x[0]))+x[0]+" "*4
  s=s[:-4]+"\n"

  for val in problems:
    x=re.split(" [+-] ",val)
    s=s+("-","+")["+" in val]+" "+" "*(max(len(x[0]),len(x[1]))-len(x[1]))+x[1]+" "*4
  s=s[:-4]+"\n"

  for val in problems:
    x=re.split(" [+-] ",val)
    s=s+"--"+"-"*max(len(x[0]),len(x[1]))+" "*4
  s=s[:-4]

  if exit:
    s=s+"\n"
    for val in problems:
      x=re.split(" [+-] ",val)
      y=int(x[0])+int(x[1]) if "+" in val else int(x[0])-int(x[1])
      s=s+" "*(2+max(len(x[0]),len(x[1]))-len(str(y)))+str(y)+" "*4
    s=s[:-4]
  return (s)
