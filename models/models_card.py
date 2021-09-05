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
        if self.texto is not None and type(self.texto) is str and self.tags is not None and type(self.tags) is list:
            return True
        else:
            return False