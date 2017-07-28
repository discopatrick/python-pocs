class CommonParent(object):
    def do_something(self):
        self.list_.append('common parent')

class First(CommonParent):
    def do_something(self):
        super(First, self).do_something()
        self.list_.append('first')

class Second(CommonParent):
    def do_something(self):
        super(Second, self).do_something()
        self.list_.append('second')

class SubClass(First, Second):

    def __init__(self):
        self.list_ = []

    def do_this(self):
        self.do_something()
