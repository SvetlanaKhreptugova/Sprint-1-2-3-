import unittest

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

from pereval.models import Pass, User, Coord, Level, Image

from pereval.serializers import PassSerializer
from pereval.tests.payloads import patch_data, valid_pass_test_data, missing_user_test_data, missing_coords_test_data, \
    missing_level_test_data, missing_images_test_data


class PassApiTestCase(APITestCase):
    def setUp(self):
        self.setup_data = Pass.objects.create(
            title="Uullua",
            user=User.objects.create(
                first_name="Gaga",
                surname="Past",
                last_name="Lady",
                email="mail1@yandex.ru",
                phone="19929394934"
            ),
            coords=Coord.objects.create(
                latitude=54.345,
                longitude=54.4534,
                height=600
            ),
            level=Level.objects.create(
                winter="1A",
                summer="1А",
                autumn="1А",
                spring="1A"
            )
        )
        self.image_1 = Image.objects.create(
            passes=self.setup_data,
            data="https://s.mediasalt.ru/cache/content/data/images/130/130083/original.jpg",
            title="foto1"
        )
        self.image_2 = Image.objects.create(
            passes=self.setup_data,
            data="https://altaitg.ru/upload/resize_cache/iblock/c65/800_500_1/c65f1a62717c5b9894e3e01ace6bc3f5.jpg",
            title="foto2"
        )

        self.setup_data_status_not_new = Pass.objects.create(
            title="Pending",
            status='PG',
            user=User.objects.create(
                first_name="Kruzenshtern",
                surname="Ivan",
                last_name="Fedorovic",
                email="qwe322@mail.ru",
                phone="87777777777"
            ),
            coords=Coord.objects.create(
                latitude=49.545,
                longitude=53.432,
                height=1100
            ),
            level=Level.objects.create(
                winter="1А",
                summer="1B",
                autumn="1B",
                spring="1А"
            )
        )
        self.image_1 = Image.objects.create(
            passes=self.setup_data,
            data="https://pereval.online/imagecache/original/object/images/2019/12/24/17d2d7-4.jpg",
            title="foto1"
        )


class BaseTestCase(PassApiTestCase):
    def setUp(self):
        self.patch_data = patch_data
        super().setUp()

    def test_get_list(self):
        url = reverse('submitData-list')
        response = self.client.get(url)
        serializer_data = PassSerializer([self.setup_data, self.setup_data_status_not_new], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('submitData-detail', args=(self.setup_data.id,))
        response = self.client.get(url)
        serializer_data = PassSerializer(self.setup_data).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_invalid_pending(self):
        url = reverse('submitData-detail', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_valid_title(self):
        url = reverse('submitData-detail', args=(self.setup_data.id,))
        new_data = {
            "title": "Ural"
        }
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('Uullua', self.setup_data.title)

    def test_get_data_by_email(self):
        response = self.client.get("/submitData/", {"user__email": "mail1@yandex.ru"})
        self.assertEqual(len(response.data), 1)

    def test_valid_patch_pending(self):
        response = self.client.patch(path=reverse("submitData-detail",
                                                  kwargs={'pk': self.setup_data.pk}),
                                     data=self.patch_data,
                                     format='json')
        self.assertEqual(response.data, {'state': 1, 'message': 'Запись успешно обновлена'})


class CreateNewPassesTest(APITestCase):
    def setUp(self):
        self.valid_pass_test_data = valid_pass_test_data
        self.missing_user_test_data = missing_user_test_data
        self.missing_coords_test_data = missing_coords_test_data
        self.missing_level_test_data = missing_level_test_data
        self.missing_images_test_data = missing_images_test_data

    def test_create_pass(self):
        url = reverse('submitData-list')
        response = self.client.post(url, data=json.dumps(self.valid_pass_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_user(self):
        url = reverse('submitData-list')
        response = self.client.post(url, data=json.dumps(self.missing_user_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_coords(self):
        url = reverse('submitData-list')
        response = self.client.post(url, data=json.dumps(self.missing_coords_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_level(self):
        url = reverse('submitData-list')
        response = self.client.post(url, data=json.dumps(self.missing_level_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_image(self):
        url = reverse('submitData-list')
        response = self.client.post(url, data=json.dumps(self.missing_images_test_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

