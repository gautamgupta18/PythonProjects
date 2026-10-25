pswd = input("Set a password: ")
uprcase = False
lwrcase = False
digit = False
spclchar = False
if " " in pswd:
  print("Password can't contain space...")
else:
  for char in pswd:
    if char.isupper():
      uprcase = True
    elif char.islower():
      lwrcase = True
    elif char.isdigit() :
      digit = True
    else:
      spclchar = True

  if( len( pswd ) >= 8 and uprcase and lwrcase and digit and spclchar ):
    print("Strong Password...")

  else:
    print("Weak password...")
    print("Password should atleast 1 uppercase, 1 lowercase, 1 Special Character and 1 digit...")