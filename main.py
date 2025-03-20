import requests

# Ваш GitHub токен
GITHUB_TOKEN = 'token'
# Ваш GitHub username
USERNAME = 'username'


headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def get_following(username):
    url = f'https://api.github.com/users/{username}/following'
    following = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            following.extend([user['login'] for user in response.json()])
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Ошибка: {response.status_code}")
            break
    return following

def get_followers(username):
    url = f'https://api.github.com/users/{username}/followers'
    followers = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            followers.extend([user['login'] for user in response.json()])
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Ошибка: {response.status_code}")
            break
    return followers


def get_follower_count(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['followers']
    else:
        print(f"Ошибка при получении данных для {username}: {response.status_code}")
        return 0


def unfollow_user(username):
    url = f'https://api.github.com/user/following/{username}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Отписались от пользователя: {username}")
    else:
        print(f"Ошибка при отписке от {username}: {response.status_code}")


def main():
    following = get_following(USERNAME)
    followers = get_followers(USERNAME)

    for user in following:
        if user not in followers:
            follower_count = get_follower_count(user)
            if follower_count < 1500:
                print(f"Пользователь {user} не подписан на вас и имеет {follower_count} подписчиков.")
                unfollow_user(user)

if __name__ == "__main__":
    main()