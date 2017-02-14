from django.test import TestCase
from foodsaving.users.factories import UserFactory
from foodsaving.users.serializers import UserSerializer


class TestUserSerializer(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = UserFactory()

    def test_instantiation(self):
        serializer = UserSerializer(self.user)
        for k in ['id', 'display_name', 'email']:
            self.assertEqual(serializer.data[k], getattr(self.user, k))
