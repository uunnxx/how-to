from flask import Flask


app = Flask(__name__)

@app.route('/search')
def get_search():
    return render_template('search.html')


@app.route('/customer/<id>', methods=['POST', 'PUT'])
def update_customer(id):
    db.update_customer(request.form)
    return redirect(url_for('get_customer', id=id, update=True))


def delete_order(self, id):
    conn = self.get_db_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM order_item WHERE order_id = {id}')
        cursor.execute(f'DELETE FROM customer_order WHERE id = {id}')


if __name__ == '__main__':
    app.run(debug=True)
