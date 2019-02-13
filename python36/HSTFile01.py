import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

buf = read_into_buffer("C:\\Work\\Github\\pyautogui\\testdata\\DeviceData.bin")


print(buf)