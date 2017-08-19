import requests

from unittest import TestCase
from unittest import mock

import main

def mock_sum(a, b):
    return a + b

class TestCalculator(TestCase):

    @mock.patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)

    @mock.patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum_with_side_effect(self, sum):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(2, 5), 7)

class TestBlog(TestCase):

    @mock.patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 2,
                'title': '테스트 타이틀',
                'body': '테스트 바디'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        assert MockBlog is main.Blog
        assert MockBlog.called
        blog.posts.assert_called_with()
        blog.reset_mock()
        blog.posts.assert_not_called()

