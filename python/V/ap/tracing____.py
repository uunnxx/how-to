# class TracingMeta(type):
#     @classmethod
#     def __prepare__(mcs, name, bases, **kwargs):
#         print('TracingMeta.__prepare__(name, bases, **kwargs)')
#         print(f'\t{mcs=}')
#         print(f'\t{name=}')
#         print(f'\t{bases=}')
#         print(f'\t{kwargs=}')
#         namespace = super().__prepare__(name, bases)
#         print(f'<--- {namespace=}')
#         print()
#         return namespace
#
#     def __new__(mcs, name, bases, namespace, **kwargs):
#         print('TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)')
#         print(f'\t{mcs=}')
#         print(f'\t{name=}')
#         print(f'\t{bases=}')
#         print(f'\t{namespace=}')
#         print(f'\t{kwargs=}')
#         cls = super().__new__(mcs, name, bases, namespace)
#         print(f'<--- {cls=}')
#         print()
#         return cls
#
#     def __init__(cls, name, bases, namespace, **kwargs):
#         print('TracingMeta.__init__(cls, name, bases, namespace, **kwargs)')
#         print(f'\t{cls=}')
#         print(f'\t{name=}')
#         print(f'\t{bases=}')
#         print(f'\t{namespace=}')
#         print(f'\t{kwargs=}')
#         cls = super().__init__(name, bases, namespace)
#         print()
#
#
# a = TracingMeta('NAME_HERE', ('bases', ), {0: 'NAMESPACE'}, first='first', second='second')
