from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_lobby_GET(self):
        client = Client(self)
        response = client.get(reverse('base:lobby'))

        self.assertEquals(response.status_code, 200)

    def test_room_GET(self):
        client = Client(self)
        response = client.get(reverse('base:room'))

        self.assertEquals(response.status_code, 200)

    # def test_getToken_GET(self):
    #     client = Client(self)
    #     response = client.get(reverse('base:getToken'))

    #     self.assertEquals(response.status_code, 200)

    # def test_createMember_GET(self):
    #     client = Client(self)
    #     response = client.get(reverse('base:createMember'))

    #     self.assertEquals(response.status_code, 200)

    # def test_getMember_GET(self):
    #     client = Client(self)
    #     response = client.get(reverse('base:getMember'))

    #     self.assertEquals(response.status_code, 200)

    # def test_deleteMember_GET(self):
    #     client = Client(self)
    #     response = client.get(reverse('base:deleteMember'))

    #     self.assertEquals(response.status_code, 200)
