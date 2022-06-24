from  Statblock import Statblock

test= Statblock("Beast_of_Ill_Omen","Beast_of_Ill_Omen.PNG")
test.set_raw()
print(test.raw().splitlines())
"""
    Common mistakes in parsing...
    + is mistaken for 4


"""

"Parsing variables that we take from the raw"
name = ""
"Flags for different parsing protocol"
name_flag = False
nextLine_flag = False #Tells to append next line rather that set only one line
for line in test.raw().splitlines():
    if len(line) > 2 and name_flag==False:
        name = line
    else:
        if len(line) > 2 and name_flag==True:
            name = line
