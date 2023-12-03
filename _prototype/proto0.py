
def read_file(file_name):
    if file_name == None:
        file_name = "./doc.txt"

    content = ""
    with open (file_name, mode="r", encoding="utf-8") as cfile:
        lines = cfile.readlines()

    for line in lines:
        content += line.strip() + "\n"

    return content

"""
txt = read_file(None)
s = Storage(txt)
print(s.get_all_notes(['congue']))
print(s.get_all_notes(['congue', 'cursus']))
print(s.get_all_notes(['cursus', 'congue']))
"""