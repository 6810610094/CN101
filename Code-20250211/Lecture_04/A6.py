import time
import os

count = 0
for hour in range(0, 24):
    for min in range(0, 60):
        for sec in range(0, 60):
            print(f"{hour:02d}:{min:02d}:{sec:02d}")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            count += 1
print(f"{count = }")
