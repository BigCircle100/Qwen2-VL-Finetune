import json
import os
import copy


templete = {
    "id": "000000033471",
    "image": "000000033471.jpg",
    "conversations": [
      {
        "from": "human",
        "value": "<image>\n你是一个抽烟检测助手，目标是读取用户输入的照片，识别图片中是否有人抽烟，回答是或否。"
      },
      {
        "from": "gpt",
        "value": "是"
      }
    ]
}
datasets = []

import os
import random
root = "datasets"
w = os.walk(root)
total = 0
for (dirpath, dirnames, filenames) in w:
    for filename in filenames:
        if str(filename).endswith(".json"):
          continue
        new_data = copy.deepcopy(templete)
        new_data["id"] = str(total)
        total += 1
        new_data["image"] = str(dirpath).split('/')[-1] + "/" + str(filename)
        new_data["conversations"][1]["value"] = "是" if str(dirpath).split('/')[-1] == '1' else "否"
        datasets.append(new_data)

random.shuffle(datasets)
with open("datasets/train_data.json","w") as f:
    json.dump(datasets, f)