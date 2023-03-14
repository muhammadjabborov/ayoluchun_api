from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category


class CourseTest(APITestCase):
    def test_get_all_category(self):
        response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/category/list/')
        self.assertEqual(response.status_code, 200)

    # def test_retrieve_category(self):
    #     response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/category/psixologiya?user_id=1')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 200)
    def test_list_course(self):
        response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/list?user_id=2')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    # def test_retrieve_course(self):
    #     response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/kasb-psixologiyasi?user_id=2')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 200)

    # def test_list_lesson(self):
    #     response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/lesson/list/kasb-psixologiyasi?user_id=2')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 200)

    def test_retrieve_certificate(self):
        response = self.client.get('http://127.0.0.1:8000/uz/api/v1/course/certificate/?user=2&course=1')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


"""
class CommentTests(APITestCase):
    def setUp(self):
        self.comment1 = Comment.objects.create(author='user1', text='comment 1')
        self.comment2 = Comment.objects.create(author='user2', text='comment 2', parent_comment=self.comment1)
        self.comment3 = Comment.objects.create(author='user3', text='comment 3', parent_comment=self.comment1)

    def test_list_comments(self):
        url = '/comments/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # Only root comments should be returned
        self.assertEqual(response.data[0]['text'], 'comment 1')
        self.assertEqual(len(response.data[0]['replies']), 2)

    def test_create_comment(self):
        url = '/comments/'
        data = {'author': 'user4', 'text': 'new comment', 'parent_comment': self.comment1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 4)

    def test_update_comment(self):
        url = f'/comments/{self.comment1.id}/'
        data = {'author': 'user1', 'text': 'updated comment'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.text, 'updated comment')

    def test_delete_comment(self):
        url = f'/comments/{self.comment2.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=self.comment2.id).exists())
"""
