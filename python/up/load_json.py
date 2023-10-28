import json


filename = "aplymouth-libraries.json"
try:
    with open(filename) as fp:
        library_data = json.load(fp)
except FileNotFoundError:
    print(f"I couldn't find the \"{filename}\" file!")


print(library_data.keys())

print(library_data["features"][0]["properties"]["LibraryName"])
