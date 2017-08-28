#!/usr/bin/env python3
import os

if not os.path.exists("swagger-codegen-cli.jar"):
    os.system(
        "wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar")

os.system(
    "java -jar swagger-codegen-cli.jar generate -i https://api.opendota.com/api -l python -o . --git-repo-id od-python --git-user-id seraphli --config config.json")
sentences = """
This project is generated for OpenDota api using swagger.

What I do:
```sh
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar
java -jar swagger-codegen-cli.jar generate -i https://api.opendota.com/api -l python -o . --git-repo-id od-python --git-user-id seraphli --config config.json
```

**NB**: Recommend using python 3, unless you want to deal with ssl error.

## Introduction

"""
with open("README.i.md", "w") as output:
    with open("README.md", "r") as input:
        lines = input.readlines()
        second_line = lines[1]
        del lines[1]
        second_line = "**" + second_line.replace("# Introduction ", "")[:-1] + "**" + "\n"
        lines.insert(1, second_line)
        for line in sentences.splitlines(keepends=True)[::-1]:
            lines.insert(1, line)
        output.writelines(lines)
os.remove("README.md")
os.rename("README.i.md", "README.md")
os.system("echo '' >> .gitignore")
os.system("echo '#swagger jar' >> .gitignore")
os.system("echo 'swagger-codegen-cli.jar' >> .gitignore")
