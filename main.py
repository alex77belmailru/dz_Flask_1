from flask import Flask, jsonify, request

app = Flask(__name__)
posts = []  # список постов [{id, owner, content}]
users = []  # список юзеров [name]


# создание пользователя
@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()['username']
    if user in users:
        return jsonify(['username already in use'])
    if not user:
        return jsonify(['username must not be empty'])
    users.append(user)
    return jsonify([f'user {user} created'])


# чтение пользователей
@app.route('/users', methods=['GET'])
def read_user():
    return jsonify(users)


# удаление пользователя
@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        users.remove(username)
        return jsonify(['user deleted'])
    return jsonify([f'user {username} not found'])


#  создание поста
@app.route('/posts', methods=['POST'])
def create_post():
    post_json = request.get_json()
    if post_json and 'content' in post_json and 'owner' in post_json:
        if post_json['owner'] not in users:
            return jsonify([f'user {post_json["owner"]} not found. create user first'])
        post = {
            'id': 1 if not posts else posts[-1]['id'] + 1,
            'content': post_json['content'],
            'owner': post_json['owner']
        }
        posts.append(post)
        return jsonify([f'post {post["id"]} created'])
    return jsonify(['the post must contain the content and the owner fields'])


# изменине поста
@app.route('/update_post/<int:post_id>', methods=['POST'])
def update_post(post_id):
    post_json = request.get_json()
    if post_json and 'content' in post_json and 'owner' in post_json:
        for post in posts:
            if post['id'] == post_id:
                i = posts.index(post)
                if post_json['owner'] not in users:
                    return jsonify([f'user {post_json["owner"]} not found. create user first'])
                post = {
                    'id': post_id,
                    'content': post_json['content'],
                    'owner': post_json['owner']
                }
                posts[i] = post
                return jsonify([f'post {post["id"]} updated'])
        return jsonify([f'post {post_id} not found'])
    return jsonify(['the post must contain the content and the owner fields'])


# чтение списка постов
@app.route('/posts', methods=['GET'])
def read_posts():
    return jsonify({'posts': posts})


# чтение поста по id
@app.route('/post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return jsonify(post)
    return jsonify([f'post {post_id} not found'])


@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return jsonify(['post deleted'])
    return jsonify([f'post {post_id} not found'])


if __name__ == '__main__':
    app.run(debug=True)
