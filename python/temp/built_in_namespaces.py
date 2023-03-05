# Built-in namespace
import builtins

# Extended subclass
class mystr(str):
    def pr(self):
        print(self)


# Substitute the original str with the subclass on the built-in namespace
builtins.str = mystr

str(1111).pr()
'1111'.pr()
# print(str(1234).pr())
# print(str(0).pr())
# print(str('').pr())
# print('0'.pr())



# class TaggedString(str):
#     """
#     A ``str`` with a ``.tags`` set and ``.kwtags`` dict of tags.
#     Usage example::
#       ts = TaggedString("hello world!", "greeting", "cliche",
#                         what_am_i="h4cker")
#       (ts.upper(), ts.tags, ts.kwtags)
#     """
#
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, args[0])
#
#     def __init__(self, s, *tags, **kwtags):
#         super().__init__()
#         self.tags = set(tags)
#         self.kwtags = kwtags
#
# ts = TaggedString('hhhh')
#
# print(ts)

class mystr(str):
    def pr(self):
        print(self)


aa = mystr('aaaaaaaaaaaa')
aa.pr()
