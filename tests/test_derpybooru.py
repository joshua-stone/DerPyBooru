import unittest
from derpibooru import Search

class DerPyBooruAPITests(unittest.TestCase):
    def test_query(self):
        """
        Test a query and make sure it returns correct image count and all images
        are valid
        """
        limit, tag = 10, "sunset shimmer"
        images = [image for image in Search().query(tag).limit(limit)]

        self.assertEqual(len(images), limit)

        for image in images:
            self.assertIsNotNone(image)
            self.assertTrue(tag in image.tags)

    def test_ascending(self):
        """
        Tests the functionality of ascending search
        """
        limit = 10
        images = [image for image in Search().ascending().limit(limit)]

        self.assertEqual(len(images), limit)

        for image in images:
            self.assertIsNotNone(image)
            """
            Must return images with IDs from 0 to 10
            """
            self.assertLessEqual(image.id_number, 10)

            """
            Check if the images are in sequential order
            by comparing the ID of the next image
            """
            try:
                nextImg = images[images.index(image) + 1]
                if nextImg is not None:
                    self.assertLess(image.id_number, nextImg.id_number)
            except IndexError:
                pass

    def test_descending(self):
        """
        Tests the functionality of descending search
        """
        limit = 10
        images = [image for image in Search().descending().limit(limit)]

        self.assertEqual(len(images), limit)

        for image in images:
            self.assertIsNotNone(image)
            """
            Check if the images are in sequential order
            by comparing the ID of the next image
            """
            try:
                nextImg = images[images.index(image) + 1]
                if nextImg is not None:
                    self.assertGreater(image.id_number, nextImg.id_number)
            except IndexError:
                pass

if __name__ == "__main__":
    unittest.main()