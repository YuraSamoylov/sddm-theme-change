#!/usr/bin/env python3

import sys

theme = sys.argv[1]
file_name = "/etc/sddm.conf"
theme_line = 11

with open(file_name, "r") as file:
    lines = file.readlines()

lines[theme_line - 1] = f"Current={theme}\n"

with open(file_name, "w") as file:
    file.writelines(lines)
