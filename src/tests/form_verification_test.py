import unittest
import form_verification

class TestFormVerification(unittest.TestCase):
    def assert_first_is_none_others_is_not_none(self, test_cases, function):
        for i, case in enumerate(test_cases):
            msg = function(case)

            if i == 0:
                self.assertIsNone(msg)
            else:
                self.assertIsNotNone(msg)


    def test_author(self):
        authors = ["Peruna", "Porkkana" * 100]

        self.assert_first_is_none_others_is_not_none(authors, form_verification.verify_author)


    def test_title(self):
        titles = ["Satsuma", "Omena" * 100]

        self.assert_first_is_none_others_is_not_none(titles, form_verification.verify_title)

    
    def test_booktitle(self):
        titles = ["Konkeli", "Mankeli" * 100]

        self.assert_first_is_none_others_is_not_none(titles, form_verification.verify_booktitle)


    def test_journal(self):
        journals = ["Kakku", "Kukka" * 100]

        self.assert_first_is_none_others_is_not_none(journals, form_verification.verify_journal)


    def test_publisher(self):
        publishers = ["Verna", "Gabriel" * 100]

        self.assert_first_is_none_others_is_not_none(publishers, form_verification.verify_publisher)


    def test_pages(self):
        pages = ["1", "9" * 100]

        self.assert_first_is_none_others_is_not_none(pages, form_verification.verify_pages)


    def test_year(self):
        years = ["2024", "-3", "12345"]

        self.assert_first_is_none_others_is_not_none(years, form_verification.verify_year)


    def test_volume(self):
        volumes = ["101", "blaablaa" * 100]

        self.assert_first_is_none_others_is_not_none(volumes, form_verification.verify_volume)