import time
import mysql.connector
import recommendations_processing

# Pooling connection is much more efficient than normal connection methods as original tests were too slow
conn_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    host="localhost",
    user="root",
    password="",
    database="users_db"
)

def get_next_request():
    """
    Description: Gets next recommendation request based on timestamp from the database
    Parameter: None
    Return: Array of a recommendation request record
    """
    connection = conn_pool.get_connection()
    with connection.cursor() as cursor:
        query = "SELECT * FROM sync_requests WHERE complete=0 ORDER BY request_timestamp LIMIT 1"
        cursor.execute(query)
        sync_row = cursor.fetchall()
    connection.close()
    return sync_row


def update_request(user_id, request_timestamp, server_output):
    """
    Description: Updates the request record with the server output post processing
    Parameter: The requesting user's id
    Parameter: The timestamp of the request
    Parameter: The server output for the request
    Return: None
    """
    connection = conn_pool.get_connection()
    with connection.cursor() as cursor:
        query = "UPDATE sync_requests SET server_output=%s, complete=1 WHERE user_id=%s AND request_timestamp=%s"
        cursor.execute(query, (server_output, user_id, request_timestamp))
        connection.commit()
    connection.close()


def process_for_recommendation(user_id, genre_id, slider_value):
    """
    Description: Server output from recommendation_processing.py returns many games, this picks the best option based on the highest tensor value
    Parameter: The requesting user's id
    Parameter: The id of the genre they are requesting
    Parameter: The slider value corresponding to 'nicheness' of the request
    Return: The server output for the request which is just the id of the game
    """
    limit_max_total_rating_count = int(slider_value*0.5)
    limit_max_total_rating = int(slider_value*8.5)
    max_total_rating = 0
    max_total_rating_count = 0
    recommended_i = -1
    while max_total_rating_count<limit_max_total_rating_count or int(max_total_rating)<limit_max_total_rating:
        max_total_rating = 0
        max_total_rating_count = 0
        game_dict_arr = recommendations_processing.main(user_id, genre_id) # gives me a 2D array with each sub-array containing the game_dict and its tensor_value
        for i in range(len(game_dict_arr)):
            game_dict = game_dict_arr[i][0]
            if game_dict["name"] != None:
                total_rating = game_dict["total_rating"]
                if total_rating==None:
                    total_rating = 0
                total_rating_count = game_dict["total_rating_count"]
                if total_rating_count==None:
                    total_rating_count = 0
                if total_rating>max_total_rating and total_rating_count>0:
                    max_total_rating = total_rating
                    if total_rating_count>max_total_rating_count:
                        max_total_rating_count = total_rating_count
                        recommended_i = i
    recommended_game_dict = (game_dict_arr[recommended_i][0])
    server_output = recommended_game_dict["id"]
    return server_output



def complete_requests():
    """
    Description: Server script which constantly will run to pick up the requests and sleep when no requests are coming in
    Parameter: None
    Return: None
    """
    traffic = 0
    while True:
        sync_row = get_next_request()
        if sync_row == []:
            traffic += 1
            if traffic == 10000:
                time.sleep(3)
                traffic = 0
        else:
            try:
                server_output = None
                sync_row = sync_row[0]
                user_id = sync_row[0]
                request_id = sync_row[1]
                request_timestamp = sync_row[2]
                slider_value = sync_row[4]
                match request_id: # match in case I add more server request types
                    case 0:
                        genre_id = sync_row[3]
                        server_output = process_for_recommendation(user_id, genre_id, slider_value)
                update_request(user_id, request_timestamp, server_output)
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    complete_requests()
