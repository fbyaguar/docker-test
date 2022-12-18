from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from src.customers.models import Profile, Technology
from src.customers.serializers import ProfileSerializer


class GetProfileTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='admin', password='170391', is_staff=True)
        self.technology = Technology.objects.create(name='Python')
        self.profile_1 = Profile.objects.create(
            first_name='Artem',
            last_name='Sindeev',
            birthdate='1991-03-17',
            contacts='artem@ukr.net',
            user=self.user,
        )
        self.profile_1.technologies.add(self.technology)
        self.profile_2 = Profile.objects.create(
            first_name='Andrew',
            last_name='Sonny',
            birthdate='1996-07-11',
            contacts='andrew@ukr.net',
            user=self.user,
        )
        self.profile_2.technologies.add(self.technology)

        self.profile_3 = {
            'first_name': 'Anton',
            'last_name': 'Denty',
            'birthdate': '1993-03-16',
            'contacts': 'denty@ukr.net',
            'user_id': self.user.id,
            'technologies': [self.technology.name],
        }

    def test_get_profiles(self):
        url = reverse('profile-list')
        response = self.client.get(url, format='json')
        serializer_data = ProfileSerializer([self.profile_1, self.profile_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(serializer_data, response.data['results'])

    def test_create_profile(self):

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        url = reverse('profile-list')
        response = self.client.post(url, self.profile_3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.all().count(), 3)

    def test_profile_serializer(self):
        serializer_data = ProfileSerializer(self.profile_1).data
        serializer_data.pop('created')
        serializer_data.pop('modified')

        expected_data = {
             'id': self.profile_1.id,
             'user': 'admin',
             'technologies': ['Python'],
             'uuid': str(self.profile_1.uuid),
             'first_name': 'Artem',
             'last_name': 'Sindeev',
             'birthdate': '1991-03-17',
             'biography': '',
             'contacts': 'artem@ukr.net'
             }

        self.assertEqual(serializer_data, expected_data)
