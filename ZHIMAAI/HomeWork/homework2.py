import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

# 获取当前脚本所在目录
SCRIPT_DIR = Path(__file__).parent
image_path=SCRIPT_DIR / 'pictures' / 'dinosaur.jpg'
# 读取图像
my_image=plt.imread(image_path)

 