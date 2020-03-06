from aiohttp import ClientSession, web
from passlib.hash import pbkdf2_sha256
from hashlib import sha256
from urllib.parse import quote


async def signup(request):
    async with ClientSession() as session:
        data = await request.json()
        password_type = data["type"]
        password = data['password']
        username = data['username']

        signup_url = request.app['config']['users']['url'] + '/v1/users/'
        get_user_url = request.app['config']['users']['url'] + '/v1/users/{}/'.format(quote(data['username'], safe=""))

        if password_type.lower() not in ["plain", "sha256"]:
            return web.json_response(data={"error": "Invalid password type"}, status=400)

        if password_type.lower() == "plain":
            password = sha256("{}_{}".format(username, password).encode()).hexdigest()

        async with session.get(get_user_url) as resp:
            if resp.status == 200:
                return web.json_response(data={"error": "This username is already taken"}, status=400)

        password_hash = pbkdf2_sha256.hash(password)
        new_data = {
            "username": username,
            "password": password_hash
        }

        async with session.post(signup_url, json=new_data) as resp:
            if resp.status == 201:
                return web.json_response(data={}, status=201)
            else:
                return web.json_response(data={"error": "Server error"}, status=201)
