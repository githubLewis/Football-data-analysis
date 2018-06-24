def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    @constant
    def INPUT_FILE():
        return 'inputs/E0.csv'
    @constant
    def OUTPUT_PATH():
        return 'outputs/'