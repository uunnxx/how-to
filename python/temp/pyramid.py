def wrapped(request, *args, **kwargs):
    """ Call the lifecycles methods with these arguments:
    Pyramid pre callbacks will receive these arguments:
    (None, request)
    Flask post callbacks will receive these arguments:
    (None, response)
    Flask failing callbacks will receive these arguments:
    (None, exception)
    """
    from pyramid.response import Response

    try:
        self.strategy.before_hook_point()
        pre_args = (request,)
        self.execute_pre_callbacks(pre_args)

        try:
            response = handler(request, *args, **kwargs)
        except Exception as e:
            if isinstance(e, Response):
                self.execute_post_callbacks(e)
            else:
                self.execute_failing_callbacks(sys.exc_info())

            raise

        return self.execute_post_callbacks(response)
    except AttackBlocked:
        is_uwsgi = 'uwsgi.version' in request.environ

        # In uwsgi 2.0.14, raising an AttackBlocked kill the connection
        # Instead return a 500 error
        if is_uwsgi:
            response = Response("Internal Server Error")
            response.status_int = 500
            return response

        raise
