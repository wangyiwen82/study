class organism(object):
    def __init__(self)
        self.live=True
        self.dead=False
class animal(organism):
    def __init__(self)
        super(animal,self).__init__()
        self.live=True
        self.dead=False
class vertebrate(animal):
    def __init__(self)
        super(vertebrate,self).__init__()
        self.run=True
        self.crawl=False
class mammal(vertebrate)
    def __init__(self)
        super(mammal,self).__init__()
        self.vivipary=True
        self.oviparity=False
