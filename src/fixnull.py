import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                content = f.read()
            # Xóa null byte
            content = content.replace(b'\x00', b'')
            with open(path, 'wb') as f:
                f.write(content)
            print(f"[SỬA] {path}")
