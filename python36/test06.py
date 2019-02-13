from data.util import md5
import os
target_folder = "C:\\Work\\Github\\pyautogui\\testdata\\test"

smf_dict = {}


for i in os.listdir(target_folder):
    smf_dict["500C1S0"] = md5(os.path.join(target_folder, i))
    print(smf_dict.keys())
    print(smf_dict.values())


    # print(md5(os.path.join(target_folder, i)))
