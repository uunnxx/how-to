for i in range(0, 4):
    # function_name = functions.get(i, 'default_action')

    exec(f"""
def function_{i}():
    print("function {i} was called")
    """)

#     exec(f"""
# def {function_name}():
#     print("function {function_name} was called")
#     """)



functions = {
    0: function_0,
    1: function_1,
    2: function_2,
    3: function_3,
}






def main(num: int):
    return functions.get(num)()


if __name__ == '__main__':
    # print(functions.get(0))

    main(3)
