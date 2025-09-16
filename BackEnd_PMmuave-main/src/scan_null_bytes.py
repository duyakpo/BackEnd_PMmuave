import os

root_dir = "D:/CNPM REAL/BackEnd_PMmuave-main/src"

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(subdir, file)
            with open(path, "rb") as f:
                content = f.read()
            if b"\x00" in content:
                print(f"[SỬA] File chứa NULL bytes: {path}")
                new_content = content.replace(b"\x00", b"")  # xoá NULL bytes
                with open(path, "wb") as f:
                    f.write(new_content)
                print(f"✅ Đã sửa xong: {path}")
