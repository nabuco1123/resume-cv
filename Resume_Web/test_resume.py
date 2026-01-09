
import unittest
from bs4 import BeautifulSoup

class TestResume(unittest.TestCase):
    def test_email_link(self):
        with open("Resume_Web/Resume_cv.html", "r") as f:
            soup = BeautifulSoup(f, "lxml")

        email_link = soup.find("a", href="mailto:juanpablomz23@gmail.com")
        self.assertIsNotNone(email_link, "The email link was not found.")

if __name__ == "__main__":
    unittest.main()
