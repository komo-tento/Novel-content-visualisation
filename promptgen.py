import re
import openai
import os
import numpy as np
from datetime import datetime


with open('./book/kumono_ito.txt',mode='r',encoding='shift-jis') as f:
    text = f.read()
    
lines = text.split('\n')
title = lines[0].strip()
author = lines[1].strip()

# ルビ、注釈などの除去
text = re.split(r'\-{5,}', text)[2]
text = re.split(r'底本：', text)[0]
text = re.sub(r'《.+?》', '', text)
text = re.sub(r'［＃.+?］', '', text)
# 全角スペース
text = re.sub(r'\u3000', '', text)
# 複数の改行
text = re.sub(r'\n+', '\n', text)
text = text.strip()
lines = text.split('\n')


for i in range(len(lines)):
    paragraph=lines[i].split()
    print(f'{i}:{paragraph}')
    


openai.api_key = os.environ.get("GPT_4_KEY")
model_name = "gpt-4"

start_time = datetime.now()

textline = input("画像生成したい文章の番号を入力してください：")

paragraph=lines[int(textline)].split()
question = f"""
Q: I am doing research on the automatic generation of images from the text of a novel. When generating a single image of an imagined landscape image from the text in the following "", in what language is the image represented? Generate the sentences with the assumption that they will be input to a diffusion model. However, the output sentences should be clear about what is where and what kind of scene is being spread out. For example, "There is a doll on a chair in a child's room" or "There is a big man and a little girl next to him in the forest". Outputs should be results only. Please use English. Output should be limited to 420 characters.「{paragraph}」
"""


response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")

prompt = response.choices[0]["message"]["content"].strip()


with open(
    f"output/output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}.txt", "w"
) as f:
    f.write(f"model: {model_name}\n")
    f.write("time: " + str(end_time - start_time) + "\n")
    f.write("question: " + question + "\n")
    f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")

start_time = datetime.now()


question = f"""
Q: If the following text is longer than 300 characters, please summarise the content of the text and output it within 300 characters. If the text is less than 300 characters, please output it as it is.「{prompt}」
"""


response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")

prompt = response.choices[0]["message"]["content"].strip()


with open(
    f"output/output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}.txt", "w"
) as f:
    f.write(f"model: {model_name}\n")
    f.write("time: " + str(end_time - start_time) + "\n")
    f.write("question: " + question + "\n")
    f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")
    
def save_value_to_file(value, filename):
    try:
        with open(filename, 'x') as file:
            file.write(str(value))
            print(f"ファイル '{filename}' を作成しました")
    except FileExistsError:
        with open(filename, 'w') as file:
            file.write(str(value))
            print(f"ファイル '{filename}' を上書きしました")

value_to_save = prompt
file_name = "prompt.txt"

save_value_to_file(value_to_save, file_name)