# Harmful
def get_formatted_user_info_worst(user):
    # Tedious to type and prone to conversion errors
    return f'Name: {user.name}, Age: {str(user.age)}, Sex: {user.sex}'


def get_formatted_user_info_slightly_better(user):
    # No visible connection between the format string placeholders
    # and values to use. Also, why do I have to know the type?
    # Don't these types all have __str__ functions?
    return 'Name: %s, Age: %i, Sex: %c' % (
        user.name, user.age, user.sex
    )


# Idiomatic
def get_formatted_user_info(user):
    """
    Clear and concise. At a glance I can tell exactly what the output
    should be. Note: this string could be returned directly, but
    the string itself is too long to fit on the page.
    """
    ', Sex: {user.sex}'.format(user=user)
    return 'Name: {user.name}, Age: {user.age}'
