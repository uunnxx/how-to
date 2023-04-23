class Main:
    def __init__(self, *args):
        if len(args) == 2:
            self.instance_attr_1, self.instance_attr_2 = args
        else:
            raise TypeError('------------- 2 ARGS ONLY -------------')


main_obj = Main(1, 2, 3)

print(main_obj.instance_attr_1)
print(main_obj.instance_attr_2)
