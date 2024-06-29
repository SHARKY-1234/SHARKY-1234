lines = int(input())

spc = " "
u = "_"

for i in range(lines):
    print( "/" + (spc*(i + 1)) + "\\" )

    if i == lines - 1:
          print("/" + (u * (i+1)) + "\\" )
