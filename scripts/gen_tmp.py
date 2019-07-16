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

# 题目难度颜色表
color = {
	'简单': "#5CB85C",
	'中等': "#F0AD4E",
	'困难': "#D9534F"
}
font_color_prefix = "<font color=color_code>"
font_color_suffix = "</font>\n\n"

ids = read_file_content("list/id.txt").split("\n")
titles = read_file_content("list/title.txt").split("\n")
levels = read_file_content("list/level.txt").split("\n")
urls = read_file_content("list/url.txt").split("\n")

for i in range(9):
	c_index = i + 1
	path = "../gitbook/Chapter" + str(c_index) + "/"
	for j in range(100):
		p_index = i * 100 + j + 1
		file_name = path + str(p_index) + ".md"
		content = "# " + str(p_index) + ". " + titles[p_index - 1].strip() + "\n\n"
		content += "### 题目链接\n\n" + urls[p_index - 1] + "\n\n"
		content += "### 题目难度\n\n"
		content += font_color_prefix.replace("color_code", color[levels[p_index - 1]]) + levels[p_index - 1] + font_color_suffix
		content += "### 思路\n\n\n\n"
		content += "### 图解\n\n无\n\n"
		content += "### 代码\n\n```python\n```"
		write_file_content(file_name, content)
