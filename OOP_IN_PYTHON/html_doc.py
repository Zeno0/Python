class Tag(object):
    
    def __init__(self, name, contents):
        self.start_tag = "<{}>" .format(name)
        self.end_tag = "</{}>" .format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self,file=file)


class Doctype(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents =[]

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for t in self._body_contents:
            self.contents += str(t)

        super().display(file=file)


class Htmldoc(object):
    
    def __init__(self, title=None):
        self._doc_type = Doctype()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self,file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == "__main__":
    my_page = Htmldoc("Demo HTML")
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub Heading')
    my_page.add_tag('p', "I am just a paragraph")
    with open('OOP_IN_PYTHON/test.html', 'w') as test_doc:
        my_page.display(file = test_doc)
    