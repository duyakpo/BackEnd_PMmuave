import os

files_to_fix = [
    r".\BackEnd_PMmuave-main\src\ticketing_app\routes.py",
    r".\BackEnd_PMmuave-main\src\ticketing_app\__init__.py"
]

for path in files_to_fix:
    with open(path, 'rb') as f:
        content = f.read()
    content = content.replace(b'\x00', b'')
    with open(path, 'wb') as f:
        f.write(content)
    print(f"[SỬA] {path} xong")
