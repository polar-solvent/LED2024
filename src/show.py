import os

dir_path = "assets/dest"
def is_frame(f):
    if f[0:6] == 'frame_' and f[-4:] == '.bmp':
        return True
    else:
        return False

frames_name = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and is_frame(f)
]
print(frames_name)