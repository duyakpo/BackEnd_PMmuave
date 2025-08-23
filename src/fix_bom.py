import os

root_dir = "D:/CNPM REAL/BackEnd_PMmuave-main/src"

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(subdir, file)
            with open(path, "rb") as f:
                content = f.read()

            fixed = False
            # Xóa BOM hoặc byte rác đầu file
            for bom in [b"\xef\xbb\xbf", b"\xff\xfe", b"\xfe\xff"]:
                if content.startswith(bom):
                    content = content[len(bom):]
                    fixed = True

            if fixed:
                print(f"[SỬA] Xóa BOM trong file: {path}")
                with open(path, "wb") as f:
                    f.write(content)
