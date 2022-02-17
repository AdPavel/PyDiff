from pathlib import Path

folder = str(input('Enter start folder: '))
prefix = str(input('Enter prefix fo delete: '))

folder_path = Path(folder)
for elem in folder_path.rglob("*"):
    if elem.name.startswith(prefix):
        elem.replace(str(elem.parent) + '/' + elem.name[10:])
        print(elem.name)
