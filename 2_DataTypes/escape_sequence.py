story =  "Corona has taken lives of many people.\n It is still infecting poeple\t."
print(story)

#\n inserts new line
#\t inserts tab
#\\ gives backslash
#\' inserts single quotes

letter = '''Dear <|Name|>,
You are selected!

Date: <|Date|>'''

name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

