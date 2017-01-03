class Document(object):
    """
    A document of a dataset.
    """
    
    def __init__(self, name, content):
        self.name = name
        self.content = content


    def __str__(self):
        return '[Document {0}]\n{1}'.format(self.name, self.content)
