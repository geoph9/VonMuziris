import subprocess, os, ast
import pandas as pd
from tqdm import tqdm
import time

df = pd.read_csv("processedSKUs_nodups.csv")
imgs = df.images.to_list()
# for img in tqdm(imgs):
#       img = ast.literal_eval(img)                          
#       for im in img:                                       
#           out_name = im.replace("?dl=0", "").split("/")[-1]
#           if os.path.isfile(out_name): continue            
#           if im.strip() == "": continue                    
#           subprocess.check_output(["wget", im, "-O", os.path.join("images", out_name)])
#           time.sleep(0.01)
         
os.makedirs("images_onlyids", exist_ok=True)
for i, img in enumerate(tqdm(imgs)):
      img = ast.literal_eval(img)
      for j, im in enumerate(img):
          out_name = f"{i}_{j}.{os.path.splitext(im.replace('?dl=0', ''))[1]}"
          print(out_name)
          if os.path.isfile(out_name): continue
          if im.strip() == "": continue
          subprocess.check_output(["wget", im, "-O", os.path.join("images_onlyids", out_name)])
          time.sleep(0.01)
