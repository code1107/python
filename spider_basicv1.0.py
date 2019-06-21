#coding:utf-8
import re
import requests
url = raw_input("please input spider url:")
response = requests.get(url)
print(response.status_code)#响应的状态码
print(response.content)#返回字节信息
print(response.text)#返回文本内容
print("----------------------------")
urls = re.findall(r'class="items".*?href="(.*?)"',response.text,re.S)#re.S把文本信息转换成1行匹配
url1 = urls[5]
result = requests.get(url1)
mp4_url = re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video = requests.get(mp4_url)
with open('D:\\a.mp4','wb') as f:
    f.write(video.content)