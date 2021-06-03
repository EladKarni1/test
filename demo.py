

f = open('test.txt', 'r')
f2= open('outputfile.txt','a')//
lines=f.readlines()//take the file and return that as a line to (lines)

titles = []
issues = []

for i in range(len(lines)):
    if lines[i].startswith("T")://if starts with "T"
        if lines[i].split(':')[1] not in titles:    //split and take location 1 and check if its not in the list "titles" already
            titles.append(lines[i].split(':')[1])   //if its not, add it to titles list
    if lines[i].startswith("Iss"):
        if lines[i].split(':')[1] not in issues:    //split and take location 1 and check if it's not in the list "issues" already
            issues.append(lines[i].split(':')[1])   //if its not,add it to issues list
    if lines[i].startswith("[ NOTE_MISSING ]"):
              if lines[i+2].startswith("Owner: chdauto") | lines[i+2].startswith("Owner: syspdbuild") | lines[i+2].startswith("Owner: syspdbuild2"):
               continue
              else:
               f2.write(lines[i])
               f2.write("@"+lines[i+2].replace("Owner: ", "").replace("\n", "")+",Please add git notes to this commit!\n")
for index, title in enumerate(titles):    //give me the location of titles and title in titles
    f2.write('[' + issues[index].replace(' ', '').replace("\n", "") + ']' + title)


f.close()
f2.close()
