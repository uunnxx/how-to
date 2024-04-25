def create_class(*atts):
    class Class:
        def __init__(self, *args):
            for att, arg in zip(atts, args):
                setattr(self, att, arg)
    return Class



Student = create_class('name', 'address', 'phone', 'gender')

tt = Student('Name', 'Address', '47306524', 'male')


print(tt.address)
