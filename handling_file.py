import json

# contents = {"aa": 12, "bb": 21}

# with open("myfile2.txt", "w") as file:
#     file.write(json.dumps(contents))

with open("myfile2.txt") as file:
    contents = file.read()

print(contents)  