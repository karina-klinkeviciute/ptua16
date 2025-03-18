from unittest.mock import patch

from service import get_posts_count


@patch('service.requests.get')
def test_get_posts_count_more_than_0(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.json.return_value = [
        {
            "userID": 1,
            "postID": 1,
            "title": "hello there",
            "content": "very nice post"
        },
        {
            "userID": 56,
            "postID": 2,
            "title": "hello to you, too",
            "content": "you also have a very nice post"
        }
    ]

    # Call the function, which will send a request to the website and then count how many posts are there.
    count = get_posts_count()

    # Test that there are more than 0 posts available on the website
    assert count > 0

def test_get_posts_count_more_than_0():
    # Call the function, which will send a request to the website and then count how many posts are there.
    count = get_posts_count()

    # Test that there are more than 0 posts available on the website
    assert count > 0

