## API, предоставляющее возможность ведения блога.
**Имеется 2 сущности:**
- Пользователь
- Пост

**Пользователь** может:
- создать
- прочитать
- изменить
- удалить пост

**Реализован функционал:**
- создание, чтение, удаление пользователя
- создание, чтение, изменение, удаление поста

Перед созданием постов имеет смысл создать пользователя.
Имя пользователя должно быть уникальным.
При создании и изменении поста в поле "owner" указывается созданный ранее пользователь, иначе пост не будет создан

## Запуск приложения

```
python main.py
```
 
## Для тестирования использовался Postman:

http://127.0.0.1:5000/users 
- GET - список пользователей
- POST - создание пользователя, в теле запроса передать JSON, например {"username": "Vasiliy"}

http://127.0.0.1:5000/delete_user/<username> - удаление пользователя с указанным username

http://127.0.0.1:5000/posts 
- GET - список постов
- POST - создание поста, в теле запроса передать JSON, например{"owner": "....", "content": "..."}

http://127.0.0.1:5000/post/<ID>  GET-запрос - чтение поста с ID 

http://127.0.0.1:5000/update_post/<ID>  POST-запрос {"owner": "....", "content": "..."} - изменение поста с ID

http://127.0.0.1:5000/delete_post/<ID>  DELETE-запрос - удаление поста с ID


## Пример исполнения команд с выводом


http://127.0.0.1:5000/users  POST-запрос с данными {"username": "Vasiliy"}:

*"user Vasiliy created"*

http://127.0.0.1:5000/users  POST-запрос с данными {"username": "Vasiliy"} с существующим username:

*"username already in use"*

http://127.0.0.1:5000/users  GET-запрос:

*"Vasiliy"*

http://127.0.0.1:5000/delete_user/Vasiliy DELETE-запрос:

*"user deleted"*

http://127.0.0.1:5000/delete_user/Vasiliy DELETE-запрос с несуществующим username:

*"user Vasiliy not found"*

http://127.0.0.1:5000/posts 
- POST-запрос с данными {"owner": "Vasily", "content": "content"} с несуществующим пользователем:

*"user Vasily not found. create user first"*
- POST-запрос с данными {"owner": "Vasily", "content": "content"}: 

*"post 1 created"*

- GET-зарпос:

*"posts": [{"content": "content","id": 1,"owner": "Vasily"}]*

http://127.0.0.1:5000/post/1  GET-запрос:

*{"content": "content","id": 1,"owner": "Vasily"}*

http://127.0.0.1:5000/update_post/1  POST-запрос с данными {"owner": "Vasily", "content": "content new"}:

*"post 1 updated"*

http://127.0.0.1:5000/delete_post/1  DELETE-запрос:

*"post deleted"*

