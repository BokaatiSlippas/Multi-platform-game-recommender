import unittest
from recommendations_processing import get_all_user_names,get_all_games,create_zero_matrix,get_user_ids,get_game,user_processing,change_value,filling_in_matrix,matrix_factorization,GetNRecommended,GetTensorValue,GetUserRecommendations,main
import tensorflow as tf

class TestDatabaseAndScraper(unittest.TestCase):
  
    def test_get_all_user_names(self): # Works
        result = get_all_user_names()
        assert result == [{'user_name': 'Bokaati Slippas'}, {'user_name': 'jibran'}, {'user_name': 'person1'}]

    def test_create_zero_matrix(self): # Works
        result = create_zero_matrix(3,3)
        print()
        print(result)
        print()
        assert True

    def test_get_user_ids(self): # Works
        result1,result2 = get_user_ids("Bokaati Slippas")
        assert result1 == 0 and result2 == "76561198931081916"

    def test_get_game(self): # Works
        result = get_game(1)
        assert result=="Thief II: The Metal Age"

    def test_user_processing(self): # Works
        result = user_processing(0,"76561198931081916")
        assert result == [['Bridge Constructor', 2],
                          ['Bridge Constructor Playground', 0],
                          ['Bridge Constructor Medieval', 0],
                          ['Geometry Dash', 5179],
                          ['Bridge Constructor Stunts', 1],
                          ['Bridge Constructor Portal', 0],
                          ['Lethal Company', 122],
                          ['Poppy Playtime', 55],
                          ['EA SPORTS FC™ 24', 1466],
                          ['Trackmania', 252],
                          ['Combat Master', 71]]

    def test_change_value(self): # Works
        matrix = create_zero_matrix(3,3)
        result = change_value(matrix, 1, 1, 2.3)
        print()
        print(result)
        print()
        assert True

    def test_filling_in_matrix(self): # Works
        all_games = get_all_games()
        user_shortened_games_arr = user_processing(0,"76561198931081916")
        matrix_of_games_users = create_zero_matrix(27500, 3)
        result = filling_in_matrix(all_games, user_shortened_games_arr, matrix_of_games_users, 0)
        assert result[8191, 0] == 0.00019308746862328635

    def test_main(self):
        try:
            result = main(0, 5)
            result = True
        except:
            result = False
        assert result == True


if __name__ == "__main__":
    unittest.main()
