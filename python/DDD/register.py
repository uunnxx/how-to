@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


###############################################################################


from user_module.application.use_cases import create_user

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_success, error = create_user(username, password)
        if is_success:
            return redirect(url_for('auth.login'))
        else:
            flash(error)

    return render_template('auth/register.html')


def create_user(username, password):
    db = get_db()

    error = None

    if not username:
        return False, 'Username is required.'
    elif not password:
        return False, 'Password is required.'
    elif db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone() is not None:
        return False, f"User {username} is already registered."

    db.execute(
        'INSERT INTO user (username, password) VALUES (?, ?)',
        (username, generate_password_hash(password))
    )
    db.commit()
    return True, None


###############################################################################


def validate_user_command(username, password):
    if not username:
        return False, 'Username is required.'
    elif not password:
        return False, 'Password is required.'
    return True, None


def create_user(username, password):
    db = get_db()
    error = None

    ok, error = validate_user_command()
    if error:
        return False, error

    if db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone() is not None:
        return False, f"User {username} is already registered."

    db.execute(
        'INSERT INTO user (username, password) VALUES (?, ?)',
        (username, generate_password_hash(password))
    )
    db.commit()
    return True, None
