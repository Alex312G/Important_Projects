#Had a file with words in format number  _  spanish word  -  english explained and made it into a dictionary {number:(spanish word,english explained)}
import json
import unicodedata
import re
file_path = "fileSpanishWords.txt"
created_file = "ParsedWords.json"
dictionary = {}
with open(file_path, "r", encoding="utf-8") as file:
    for i, line in enumerate(file, start = 1):
        line = line.strip()
        line = line.replace(f"{i}  _  ", "")
        spanish, english = re.split(r"\s*-\s*", line, maxsplit=1)
        dictionary[i] = (spanish,english) 
with open(created_file, "w") as file:   
    json.dump(dictionary, file, indent = 4)



#finalwords = unicodedata.normalize("NFKD", content)
#finalwords = finalwords.replace("“", '"').replace("”", '"')

#with open(file_path, "w", encoding = "utf-8") as file:
#    file.write(finalwords)

