class Comment:

    def __init__(self, type, memberof, description = '// todo', author = 'evildoer', showAuthor = False):
        self.type = type
        self.memberof = memberof
        self.description = description
        self.author = author
        self.showAuthor = showAuthor


    def getComment(self):
        comment = """
  /**
   * @description """ + self.description + """
   * @type { """ + self.type + """ }
   * @memberof """ + self.memberof
        if(self.showAuthor):
            comment = comment + """
   * @author """ + self.memberof
        comment = comment + """
   */"""
        return comment




