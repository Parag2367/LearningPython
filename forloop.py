# parrot = "Norwegian Blue"
#
# for char in parrot:
#     print(char)

quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine,Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"""
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Uchar =""
for char in quote:
    if char in upper:
        Uchar = Uchar + char
print(Uchar)


