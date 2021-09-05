class Tag:
    def __init__(self, req):
        if 'name' in req:
            self.name = req['name']
        else:
            self.name = None
    def validate(self):
        if self.name is not None and type(self.name) is str:
            return True
        else:
            return False