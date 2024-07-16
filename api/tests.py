import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Worker, Store, Visit

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def worker():
    return Worker.objects.create(name="Тестовый Работник", phone_number="123456789")

@pytest.fixture
def store(worker):
    return Store.objects.create(name="Тестовая Торговая Точка", worker=worker)

@pytest.mark.django_db
def test_get_stores(api_client, worker, store):
    url = reverse('store-list')
    api_client.credentials(HTTP_AUTHORIZATION='Phone 123456789')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Тестовая Торговая Точка"

@pytest.mark.django_db
def test_get_stores_no_worker(api_client):
    url = reverse('store-list')
    api_client.credentials(HTTP_AUTHORIZATION='Phone 000000000')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_create_visit(api_client, worker, store):
    url = reverse('visit-create')
    api_client.credentials(HTTP_AUTHORIZATION='Phone 123456789')
    data = {
        "store_id": store.id,
        "latitude": 55.7558,
        "longitude": 37.6176
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['latitude'] == 55.7558
    assert response.data['longitude'] == 37.6176

@pytest.mark.django_db
def test_create_visit_invalid_store(api_client, worker):
    url = reverse('visit-create')
    api_client.credentials(HTTP_AUTHORIZATION='Phone 123456789')
    data = {
        "store_id": 999,
        "latitude": 55.7558,
        "longitude": 37.6176
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_unauthorized_access(api_client):
    url = reverse('store-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_create_visit_invalid_coordinates(api_client, worker, store):
    url = reverse('visit-create')
    api_client.credentials(HTTP_AUTHORIZATION='Phone 123456789')
    data = {
        "store_id": store.id,
        "latitude": "invalid",
        "longitude": "invalid"
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
