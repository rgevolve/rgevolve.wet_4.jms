import unittest

class TestPackage(unittest.TestCase):

    def test_import(self):
        from rgevolve.wet_4.jms._version import __version__
        self.assertIsInstance(__version__, str)

