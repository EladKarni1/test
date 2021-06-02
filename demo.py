

f = open('test.txt', 'r')
lines=f.readlines()

titles = []
issues = []

for i in range(len(lines)):
    if lines[i].startswith("T"):
        if lines[i].split(':')[1] not in titles:
            titles.append(lines[i].split(':')[1])
    if lines[i].startswith("Iss"):
        if lines[i].split(':')[1] not in issues:
            issues.append(lines[i].split(':')[1])
    if lines[i].startswith("[ NOTE_MISSING ]"):
              if lines[i+2].startswith("Owner: chdauto") | lines[i+2].startswith("Owner: syspdbuild") | lines[i+2].startswith("Owner: syspdbuild2"):
               continue
              else:
               print(lines[i].replace("\n", ""))
               print("@"+lines[i+2].replace("Owner: ", "").replace("\n", "")+",Please add git notes to this commit!\n")
for index, title in enumerate(titles):
    print('[' + issues[index].replace(' ', '').replace("\n", "") + ']' + title)


f.close()
