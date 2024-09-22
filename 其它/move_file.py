import os
import shutil

for file in os.listdir("../../算法工程师学习路线"):
    if os.path.isdir(f"../../算法工程师学习路线/{file}"):
        for f in os.listdir(f"../../算法工程师学习路线/{file}"):
            # print(f)
            if f[-4:] == ".zip" and (f not in os.listdir(f"../../算法工程师学习路线/学习视频")):
                # print(f)
                shutil.move(f"../../算法工程师学习路线/{file}/{f}", f"../../算法工程师学习路线/学习视频")
