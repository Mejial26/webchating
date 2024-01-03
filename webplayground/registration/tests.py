from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.       Pruebas Unitarias
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test2','test2@gmail.com','Chocolate301')
    
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test2').exists()
        self.assertEqual(exists, True)