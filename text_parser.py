# Gets text from a site and only selects the lines matching
import re

all_matches = ""

file = open("input.txt", encoding="utf8")
regex = re.compile("(.*)url\((.*)\)(.*)")
for line in file:
    match = regex.match(line)
    if match:
        line = match.group(2)
        all_matches += f"{line}\n"

with open('cute.txt', 'w+') as f:
    f.write(all_matches)
