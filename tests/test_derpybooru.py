import unittest
from derpibooru import Search

class DerPyBooruAPITests(unittest.TestCase):
    def testquery(self):
        """Test a query and make sure it returns correct image count 
           and all images are valid"""
        max = 10
        images = []
        tag = "sunset shimmer"
        for i in Search().query(tag).limit(max): images.append(i)
        self.assertEqual(len(images), max)
        for i in images:
            self.assertIsNotNone(i)
            self.assert_(tag in i.tags)

    def testascending(self):
        max = 10
        images = []
        for i in Search().ascending().limit(max): images.append(i)
        self.assertEqual(len(images), max)

        for i in images:
            self.assertIsNotNone(i)
            # Must return images with IDs from 0 to 10
            self.assertLessEqual(i.id_number, 10)
            """Check if the images are in sequential order
                by comparing the ID of the next image"""
            try:
                nextImg = images[images.index(i) + 1]
                if nextImg is not None:
                    self.assertLess(i.id_number, nextImg.id_number)
            except IndexError:
                pass

    def testdescending(self):
        max = 10
        images = []
        for i in Search().descending().limit(max): images.append(i)
        self.assertEqual(len(images), max)

        for i in images:
            self.assertIsNotNone(i)
            """Check if the images are in sequential order
                by comparing the ID of the next image"""
            try:
                nextImg = images[images.index(i) + 1]
                if nextImg is not None:
                    self.assertGreater(i.id_number, nextImg.id_number)
            except IndexError:
                pass

if __name__ == "__main__":
    unittest.main()