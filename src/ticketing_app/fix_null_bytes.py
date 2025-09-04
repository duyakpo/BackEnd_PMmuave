import os
import shutil

root_dir = "D:/CNPM REAL/BackEnd_PMmuave-main/src"

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(subdir, file)
            with open(path, "rb") as f:
                content = f.read()
            if b"\x00" in content:
                print(f"[SỬA] File chứa NULL bytes: {path}")
                # Backup file gốc
                backup_path = path + ".bak"
                shutil.copy2(path, backup_path)
                print(f"   📂 Backup: {backup_path}")

                # Xóa NULL bytes và ghi lại file
                new_content = content.replace(b"\x00", b"")
                with open(path, "wb") as f:
                    f.write(new_content)
                print(f"   ✅ Đã sửa: {path}")
