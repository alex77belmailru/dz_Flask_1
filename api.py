from flask import Flask, jsonify, request

from logic import users, posts, delete, store, update, get_post

app = Flask(__name__)


# создание пользователя
@app.route('/users', methods=['POST'])
def create_user():
    user_json = request.get_json()
    return store(user_json)


# чтение пользователей
@app.route('/users', methods=['GET'])
def read_user():
    return jsonify(users)


# удаление пользователя
@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    return delete('user', username)


#  создание поста
@app.route('/posts', methods=['POST'])
def create_post():
    post_json = request.get_json()
    return store(post_json)


# изменение поста
@app.route('/update_post/<int:post_id>', methods=['POST'])
def update_post(post_id):
    post_json = request.get_json()
    return update(post_id, post_json)


# чтение списка постов
@app.route('/posts', methods=['GET'])
def read_posts():
    return jsonify({'posts': posts})


# чтение поста по id
@app.route('/post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    return get_post(post_id)


# удаление поста
@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return delete('post', post_id)


if __name__ == '__main__':
    app.run(debug=True)
