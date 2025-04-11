from flask_blog import app


if __name__ == '__main__':
    app.run(debug=True)


# def print_dec(print_func):
#     def wrapper(*args, **kwargs):
#         print('-' * 80)
#         print_func(*args, **kwargs)
#         print('-' * 80)
#     return wrapper
#
#
# @print_dec
# def p(values='', sep='', end='', file='', flush=''):
#     if values:
#         print(values, sep, end, file, flush)
#     else:
#         print('#' * 80)
#
#
#
#
# p('hi there')
#
# p()
