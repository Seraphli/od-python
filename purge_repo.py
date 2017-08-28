#!/usr/bin/env python3
import os
import shutil

WHITE_LIST = [".git", "config.json", "regenerate.sh", "generate.py", "purge_repo.py","swagger-codegen-cli.jar"]

root, dirs, files = next(os.walk("."))
for d in dirs:
    if d in WHITE_LIST:
        continue
    shutil.rmtree(d, ignore_errors=True)
for f in files:
    if f in WHITE_LIST:
        continue
    os.remove(f)
