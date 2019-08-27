class Inspectmodule(object):

    def __init__(self, module, class_name):
        self.module = module
        self.class_name = class_name

    # find all classes in a module
    def find_class(self):
        md = self.module.__dict__
        class_list = [md[c] for c in md if (isinstance(md[c], type) and md[c].__module__ == numpy.__name__)]
        return class_list

    # find all methods in a class
    def find_methods(self):
        cd = self.class_name.__dict__
        method_list = (list(cd))
        return method_list

import numpy
numpy_class = Inspectmodule(numpy, numpy.ndarray)
#print(numpy.array(numpy_class.find_class()).T)
print(numpy.array(numpy_class.find_methods()).T)