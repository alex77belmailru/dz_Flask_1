posts = []  # список постов в формате [{id, owner, content}]
users = []  # список юзеров в формате [name]


def store(data):
    """Сохраняет данные в posts или users"""
    if 'username' in data:  # сохраняем пользователя
        user = data['username']
        if user in users:
            return 'username already in use', 404
        if not user:
            return 'username must not be empty', 404
        users.append(user)
        return f'user {user} created', 201

    if 'owner' in data and 'content' in data:  # сохраняем пост
        if data['owner'] not in users:
            return f'user {data["owner"]} not found. create user first', 404
        post = {
            'id': 1 if not posts else posts[-1]['id'] + 1,
            'content': data['content'],
            'owner': data['owner']
        }
        posts.append(post)
        return f'post {post["id"]} created', 201

    return 'No valid data in request', 404


def get_post(post_id):
    """Возвращает один пост по его id"""
    for post in posts:
        if post['id'] == post_id:
            return post
    return f'post {post_id} not found'


def delete(*data):
    """Удаляет данные из posts или users"""
    if data[0] == 'user':  # удаляем пользователя
        user = data[1]
        if user in users:
            users.remove(user)
            return f'user {user} deleted', 201
        return f'user {user} not found', 404

    if data[0] == 'post':  # удаляем пост
        post_id = data[1]
        for post in posts:
            if post['id'] == post_id:
                posts.remove(post)
                return f'post {post_id} deleted', 201
        return f'post {post_id} not found', 404


def update(*data):
    """Изменяет данные post по его id"""
    if isinstance(data[1], dict) and 'owner' in data[1] and 'content' in data[1]:  # есть нужные поля в словаре?

        post_id = data[0]
        post_owner = data[1]['owner']
        post_content = data[1]['content']

        if post_owner not in users:
            return f'user {post_owner} not found. create user first', 404

        for post in posts:
            if post['id'] == post_id:  # пост есть в бд?
                i = posts.index(post)
                post = {
                    'id': post_id,
                    'content': post_owner,
                    'owner': post_content
                }
                posts[i] = post
                return f'post {post_id} updated', 201
        return f'post {post_id} not found', 404

    else:
        return 'No valid data in request', 404
