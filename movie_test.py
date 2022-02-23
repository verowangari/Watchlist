import unittest
from models import movie
Movie=movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Testclass to test the behavior of the Movie Class
    '''
    def setUp(self):
        '''
        Setup method that will run before every test
        '''
        self.new_movie=Movie(1234,'Python Must Be Crazy','A thrilling new python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance (self):
        self.assertTrue(isinstance(self.new_movie,Movie))
        
if __name__ == '__main__':
    unittest.main()