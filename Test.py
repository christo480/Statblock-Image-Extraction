from  Statblock import Statblock
test= Statblock("Beast_of_Ill_Omen","Beast_of_Ill_Omen.PNG")
test.set_raw()
"""print(test.raw().splitlines())"""
"""
    Common mistakes in parsing...
    + is mistaken for 4


"""
print(test.raw())

"Parsing variables that we take from the raw"
creature_name = ""
size = ""
creature_type = ""
alignment = ""
armor_class = ""
armor_type = ""
hit_points = ""
hit_dice = ""


name_flag = False
"Flag for finishing name parse protocol"
creature_info_flag=False
"Flag for finishing creature_info parse protocol"
armor_class_flag = False
"Flag for finishing armor_class parse protocol"
hit_points_flag=False
"Flag for finishing hitpoints parse protocol"
nextLine_flag = False 
"Flag for telling to capture next line in addition to current"

#Tells to append next line rather that set only one line
for line in test.raw().splitlines():
    if len(line) > 2 and name_flag==False:
        creature_name = line
        print(creature_name)
        name_flag=True
    else:
        
        if name_flag==True and len(line) > 2 and creature_info_flag==False:
            """Captured Raw Line"""
            print(line)
            creature_info_raw= line.split(",")
            creature_info_raw2= creature_info_raw[0].split(" ")
            size = creature_info_raw2[0]
            creature_type = creature_info_raw2[1]
            alignment = creature_info_raw[1]
            print(creature_info_raw)
            creature_info_flag=True
        elif len(line) > 2 and armor_class_flag==False:
            print(line)
            creature_info_raw= line.split(" ")
            print(creature_info_raw)
            armor_class = creature_info_raw[2]
            armor_type = str(creature_info_raw[2]+creature_info_raw[3])
            armor_class_flag= True
        elif len(line) > 2 and hit_points_flag==False:
            print(line)
            creature_info_raw= line.split(" ")
            print(creature_info_raw)
            hit_points = int(creature_info_raw[2])
            for i in range(3,len(creature_info_raw)):
                hit_dice+=creature_info_raw[i]
            hit_points_flag= True


            
