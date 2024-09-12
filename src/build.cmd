
py -m nuitka --standalone --onefile --windows-console-mode=disable^
 --enable-plugin=tk-inter^
 --output-dir="__build"^
 --deployment --python-flag="-OO" --python-flag="-S"^
 --output-filename="calculator.exe"^
 main.py

py -m nuitka --standalone --onefile --windows-console-mode=disable^
 --output-dir="__build"^
 --deployment --python-flag="-OO" --python-flag="-S"^
 --output-filename="update.exe"^
 payload.py
