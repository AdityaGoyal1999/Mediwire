from django.test import TestCase, Client

# Create your tests here.

class FrontEnd(TestCase):

    def test_index(self):
        """ Tests if the index page is working.
        """
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_platform_page(self):
        """ Tests if the platform page works.
        """

        c = Client()
        response = c.get("/platform/")
        self.assertEqual(response.status_code, 200)

    def test_covid_info_page(self):
        """ Tests if the covid info page works.
        """

        c = Client()
        response = c.get("/covid/")
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """ Tests if the login page works.
        """

        c = Client()
        response = c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """ Tests if the signup page works.
        """

        c = Client()
        response = c.get("/signup/")
        self.assertEqual(response.status_code, 200)