try:
    self.fail('Opps')
except Exception as ex:
    result = 'exception handled'
    ex2 = ex
    print(result)
    print(isinstance(ex2, Exception))
    print(isinstance(ex2, RuntimeError))
    print(ex2.args[0])
