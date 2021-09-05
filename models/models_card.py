class Card:
    def __init__(self, req):
        if 'texto' in req:
            self.texto = req['texto']
        else:
            self.texto = None
        if 'tags' in req:
            self.tags = req['tags']
        else:
            self.tags = None

    def validate(self):
        code = 0
        if self.texto is not None and type(self.texto) is str:
            code += 2
        if self.tags is not None and type(self.tags) is list:
            code += 4
        elif self.tags is not None and type(self.tags) is not list:
            code += 8
        if code == 6:
            return True
        if code == 2:
            return True
        else:
            return False
