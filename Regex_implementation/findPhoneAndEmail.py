import pyperclip, re

phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )""",
    re.VERBOSE,
)


emailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # top-level domain
    )""",
    re.VERBOSE,
)

text = str(pyperclip.paste())

matches = []


allPhones = phoneRegex.findall(text)
allEmails = emailRegex.findall(text)
for email in allEmails:
    print(email[0])

print(allEmails)

