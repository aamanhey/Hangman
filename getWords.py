easy_lines = open("easy_words.txt","r").read()
medium_lines = open("medium_words.txt","r").read()
hard_lines = open("hard_words.txt","r").read()
#print(lines)
#line = lines[0]
easy_words = easy_lines.split("\n")
medium_words = medium_lines.split("\n")
hard_words = hard_lines.split("\n")
#print(words)
print("--------------------Duplicates in easy and hard----------------------")
for eachWord in easy_words:
    if eachWord in hard_words:
        print(eachWord)
print("--------------------Duplicates in medium and hard------------------------")
for eachWord in medium_words:
    if eachWord in hard_words:
        print(eachWord)