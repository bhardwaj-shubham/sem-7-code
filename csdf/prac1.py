import re


def match_re(data, *args):
    for regstr in args:
        match_obj = re.search(regstr + ".*", data, re.M | re.I)
        if match_obj:
            print(match_obj.group(0).lstrip().rstrip())
        else:
            print("No", regstr, "found")


filename = input("Enter the path for email header file:")
fo = open(filename, "r")
data = fo.read()
match_re(data, "MIME-version", "Date:", "Subject:", "Delivered-to:", "From:", "^to:")
fo.close()
