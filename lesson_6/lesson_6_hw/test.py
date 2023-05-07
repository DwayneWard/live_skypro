filename = "user_data.txt"

f = open(filename, 'r', encoding='utf-8')
name = f.readline().replace('\n', '')
surname = f.readline().replace('\n', '')
email = f.readline().replace('\n', '')
phone = f.readline().replace('\n', '')


print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")

import psutil

for process in psutil.process_iter():
    try:
        files = process.open_files()
        if files:
            print(f"Process {process.name()} ({process.pid}) has {len(files())} open files:")
            for file in files:
                print(file.path)
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

