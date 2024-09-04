import unittest
from complete_requests import get_next_request,update_request,process_for_recommendation,complete_requests
import datetime

class TestDatabaseAndScraper(unittest.TestCase):
    
    def test_get_next_request(self):
        result = get_next_request()
        assert result == [(2, 0, datetime.datetime(2024, 4, 6, 18, 34, 56), 14, 5, 0, None)]
      
    def test_update_request(self):
        try:
            update_request(2, datetime.datetime(2024, 4, 6, 18, 35, 1), 7574)
            result = True
        except:
            result = False
        assert result == True
      
    def test_process_for_recommendation(self):
        result1 = process_for_recommendation(2, 14, 5)
        result2 = process_for_recommendation(2, 14, 5)
        assert result1 != result2


if __name__ == "__main__":
    unittest.main()
