import requests


def get_posts_count() -> int:
    # Get posts from a website
    response = requests.get('http://jsonplaceholder.typicode.com/posts')

    # Count how many there are
    total = len(response.json())

    return total

print(get_posts_count())

