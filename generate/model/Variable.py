class Variable:
    def __init__(self, var, type):
        self.var = var
        self.type = type


import re

if __name__ == '__main__':

    path = "./Course.java"
    file = open(path,'r',encoding='utf-8')
    content = file.read()

    # 类名规则
    class_rule = 'class\s*([0-9a-zA-Z_]*)'
    # 描述规则
    description = '.*?@ApiModelProperty\("(.*?)"\)'
    # 类型规则
    type_rule = 'private\s*([0-9a-zA-Z_]*)'
    # 变量规则
    variable = 'private\s*[0-9a-zA-Z_]*\s*([0-9a-zA-Z_]*)'
    # 匹配类名
    name = re.findall(class_rule, content)
    # 匹配描述
    des = re.findall(description, content)
    # 匹配类型
    type = re.findall(type_rule, content)
    # 匹配变量
    vars = re.findall(variable, content)
    print("end")