# Gets text from a site and only selects the lines matching
import re

all_matches = ""

file = open("cute2.html", encoding="utf8")


regex = re.compile("(.*)url\((.*)\)(.*)")
regex = re.compile("(.*)srcset=\"https://images\.unsplash\.com/photo-(.*)\?ixlib=rb-1\.2\.1(.*)")
regex = re.compile("[0-9]+\. (.*)")

for line in file:
    match = regex.match(line)
    if match:
        line = match.group(1)
        line = line.split("?")[0]
        # all_matches += f"https://images.unsplash.com/photo-{line}\n"
        all_matches += f"{line}\n"
    else:
        print(f"Skipping {line}")

with open('output.txt', 'w+') as f:
    f.write(all_matches)
