with open("vocabs_idioms.txt", "r", encoding="utf-8" ) as file:
    t = file.readlines()

with open("vocabs_idioms.md", 'w', encoding="utf-8") as file_:
    for i in t:
        if i=="\n":
            continue
        file_.write("### ")
        file_.write(i)
            