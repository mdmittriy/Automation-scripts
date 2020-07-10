import re

# re = regex = regular expression
phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d{3}-\d{4})")  # raw string  r"..."
#                       group 1 ^^   gr 2 ^^^^^
# Now the phoneNumRegex variable contains a Regex object.

# mo = matching object
mo = phoneNumRegex.search("asdfa fds afkajsd f (123) 456-7890sadfasdfasdfc")
if not mo:
    print("not found")

print(mo.group())  # ==  print(mo.group(0))
print(mo.group(1))
print(mo.group(2))

# all groupS
print(mo.groups())

# .   ^  $  *  +  ?  {  }  [  ]  \  |  (  )
# escape them using
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)
print("\n")

# | is called a pipe  and it means 'or'
heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

print("\n")

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

print("\n")

confa = re.compile(r"u(e)?ber(marginal)?|eji")
mo = confa.search("uebermargggginal priexal domoi k eji")
print(mo.group())

print("\n")

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

mo3 = batRegex.search("The Adventures of Batwowowowoman")
print(mo3.group())

# While * means “match zero or more,” the + (or plus) means “match one or
# more.”

print("\n")

haRegex = re.compile(r"(Ha){2,7}")
mo1 = haRegex.search("HaHaHaHaHaHa")
print(mo1.group())

nongreedyHaRegex = re.compile(r"(Ha){2,7}?")  # ? is added
mo2 = nongreedyHaRegex.search("HaHaHaHaHaHa")
print(mo2.group())

mo2 = haRegex.search("Ha")
print(mo2)

print("\n")

xmasRegex = re.compile(r"\d+\s\w+")
print(
    xmasRegex.findall(
        "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
    )
)
