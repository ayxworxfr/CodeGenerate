import os
import re

class Generator:
    variables = []
    comments = []

    def __init__(self, source = "Java", destination = "TypeScript", author = "evildoer", showAuthor = False):
        self.source = source
        self.destination = destination
        self.author = author
        self.showAuthor = showAuthor

    # 解析文件
    def parseFile(self, path):
        if not os.path.exists(path):
            print("文件不存在！")
            return
        file = open(path,'r',encoding='utf-8')
        content = file.read()

        class_rule = 'class\s*([0-9a-zA-Z_]*)'
        description = '.*?@ApiModelProperty\("(.*?)"\)'
        type_rule = 'private\s*([0-9a-zA-Z_]*)'
        variable = 'private\s*[0-9a-zA-Z_]*\s*([0-9a-zA-Z_]*)'
        # 匹配类名
        name = re.findall(class_rule, content)
        # 匹配描述
        des = re.findall(description, content)
        # 匹配类型
        type = re.findall(type_rule, content)
        # 匹配变量
        vars = re.findall(variable, content)



    # 转换变量类型
    def convertToTypeScript(self):
        count = 0
        for var in self.variables:
            type = var.type.trim()
            if type == "String":
                self.variables[0].type = "string"
            elif type == "Integer" or type == "Double" or type == "Long":
                self.variables[0].type = "number"
            elif type == "Date" or type == "DateTime" or type == "LocalDate" or type == "LocalTime":
                self.variables[0].type = "Date"
            else:
                self.variables[0].type = "any"


from model import Comment

if __name__ == '__main__':
    # generator = Generator()

    comment = Comment("int", "Course")
    print(comment.getComment())
    # print("aa")