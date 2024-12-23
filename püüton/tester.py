numbrid = open("telefoninumbrid.txt", "r") 


numbrid_list = list(numbrid.read())
tnumbrid = "".join(numbrid_list)
ent_numbrid = tnumbrid.replace("\n", "")

ptxt = ent_numbrid.replace("85", "!!!!!!!!!!!!!!!!!!!!")
vastus = ent_numbrid.count("85")
a = [8564427, 8542223, 8521791, 8565232, 8529283, 8586478]
a.sort()
a = str(a)
vastus = "".join(a)
print(vastus)