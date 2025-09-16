import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                content = f.read()
            # Remove BOM UTF-8
            if content.startswith(b'\xef\xbb\xbf'):
                content = content[3:]
                with open(path, 'wb') as f:
                    f.write(content)
                print(f"[SỬA BOM] {path}")
