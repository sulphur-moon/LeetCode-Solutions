# 读取文件
def read_file_content(file_name):
	content = None
	with open(file_name, "r", encoding="utf-8") as f:
		content = f.read()
		f.close()
	return content

# 写入文件
def write_file_content(file_name, content):
	with open(file_name, "w", encoding="utf-8") as f:
		f.write(content)
		f.close()
	return

ids = read_file_content("list/id.txt").split("\n")
titles = read_file_content("list/title.txt").split("\n")
levels = read_file_content("list/level.txt").split("\n")
urls = read_file_content("list/url.txt").split("\n")

# print(ids)
# print(titles)
# print(levels)
# print(urls)

content = ""
for i in range(9):
	c_index = i + 1
	content += "* [第 " + str(c_index) + " 章](Chapter" + str(c_index) + "/README.md)\n"
	for j in range(100):
		p_index = i * 100 + j + 1
		content += "\t* [" + str(p_index) + ". " + titles[p_index - 1].strip() + "](Chapter" + str(c_index) + "/" + str(p_index) + ".md)\n"
write_file_content("toc.txt", content)