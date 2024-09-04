import pymysql
from steam import Steam
from decouple import config
import polars as pl
import tensorflow as tf



def get_all_user_names():
    """
    Description: Gets an array of all the usernames in the users database
    Parameter: None
    Return: Array of usernames
    """
    connection = pymysql.connect(host='localhost', user='root', password='', database='users_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT user_name FROM users ORDER BY user_id")
    users = cursor.fetchall()
    cursor.close
    connection.close
    return users



def get_all_games():
    """
    Description: Gets an array of all the games in the games database
    Parameter: None
    Return: 2D array of the games table from the games database, with each sub array being a record of a game
    """
    connection = pymysql.connect(host='localhost', user='root', password='', database='games_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM games")
    all_games = (cursor.fetchall())
    cursor.close
    connection.close
    return all_games



def create_zero_matrix(rows, columns):
    """
    Description: Creates a polars matrix of 0s defined by the rows and columns parameters
    Parameter: Rows is first dimension of the dataframe matrix
    Parameter: Column is second dimension of the dataframe matrix
    Return: polars Dataframe of dimensions rows * columns
    """
    data = {f"user_{c}": [0.0 for r in range(rows)] for c in range(columns)}
    return pl.DataFrame(data)



def get_user_ids(user_name):
    """
    Description: Gets a specific user's id and steam id
    Parameter: The specific user's username
    Return: The user's id from the users database
    Return: The user's steam id from the users database
    """
    connection = pymysql.connect(host='localhost', user='root', password='', database='users_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT user_id,user_steam_id FROM users WHERE user_name='{user_name}'")
    id_dict = (cursor.fetchall())[0]
    cursor.close()
    connection.close()
    user_id = id_dict["user_id"]
    user_steam_id = id_dict["user_steam_id"]
    return user_id,user_steam_id



def get_game(game_id):
    """
    Description: Gets a game's name from its game id
    Parameter: A game's corresponding id in the games database
    Returns: The name of the game
    """
    connection = pymysql.connect(host='localhost', user='root', password='', database='games_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM games WHERE id='{game_id}'")
    game_name = ((cursor.fetchall())[0])["name"]
    cursor.close
    connection.close
    return game_name



def user_processing(user_id, user_steam_id):
    """
    Description: Returns a specific user's list of games along with their playtimes using the steam API
    Parameter: The user's id in the database
    Parameter: The user's steam id
    Returns: 2D array of games, with each sub array containing the playtime associated with each game for the user
    """
    KEY = config("STEAM_API_KEY")

    steam = Steam(KEY)

    user_owned_games = {}
    if user_steam_id!=None:
        user_owned_games = steam.users.get_owned_games(user_steam_id)
    user_shortened_games_arr = []
    if user_owned_games!={}:
        user_games_arr = user_owned_games["games"]
        for game_dict in user_games_arr:
            user_shortened_games_arr.append([game_dict["name"], game_dict["playtime_forever"]])
    connection = pymysql.connect(host='localhost', user='root', password='', database='users_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT game_id,playtime FROM users_games WHERE user_id='{user_id}'")
    extras_dict = (cursor.fetchall())
    cursor.close()
    connection.close()
    for i in range(len(extras_dict)):
        game_id = (extras_dict[i])["game_id"]
        game_name = get_game(game_id)
        user_shortened_games_arr.append([game_name, (extras_dict[i])["playtime"]])
    return user_shortened_games_arr



def change_value(matrix, row, column, new_value):
    """
    Description: Changes a specific value within a polars dataframe matrix
    Parameters: The users-games dataframe matrix
    Parameter: The row for the new value
    Parameter: The column for the new value
    Parameter: The new value itself
    Returns: The new updated dataframe matrix
    """
    matrix[row, column] = new_value
    return matrix



def filling_in_matrix(all_games, user_shortened_games_arr, matrix_of_games_users, index_of_user):
    """
    Description: Fills the user-game dataframe matrix using the data from the database and the newly-aquired data from the steam API for each user
    Parameter: Array of all games
    Paramater: Array of all of the user's games
    Parameter: Users-games dataframe matrix
    Parameter: The index of the user we are filling in data for
    Returns: The matrix of users-games filled with the data of the current user
    """
    current_index = 0
    user_games_index_arr = []
    temp_user_shortened_games_arr = []
    for game_dict in all_games:
        for users_game in user_shortened_games_arr:
            if users_game[0] in game_dict["name"] and users_game[1] != 0:
                user_games_index_arr.append(current_index)
                temp_user_shortened_games_arr.append(users_game)
                break
        current_index+=1
    user_shortened_games_arr = temp_user_shortened_games_arr
    #Now I have a list of all the games the user has played that are actually in my database and their corresponding rows from the 27500 games
    max_mins = 0
    for game in user_shortened_games_arr:
        if game[1]>max_mins:
            max_mins = game[1]
    #max_mins so I can normalise data between 0 and 1
    for game in user_shortened_games_arr:
        game[1] = game[1]/max_mins
    #normalisation works
    #now want a matrix of users against games with each user,game combination containing the normalised data of mins played which is games[1]
    current_index = 0
    for game in user_shortened_games_arr:
        matrix_of_games_users = change_value(matrix_of_games_users, user_games_index_arr[current_index], index_of_user, game[1])
        current_index+=1
    #matrix is filled in properly now
    return matrix_of_games_users



def matrix_factorization(user_game_matrix, num_users, num_games, latent_features, learning_rate, epochs):
    """
    Description: Performs machine learning on the new user-latent_features and games-latent_features matrices towards the users-games matrix
    Parameter: The users-games matrix to learn towards
    Parameter: The number of users in the users database
    Parameter: The number of games in the games database
    Parameter: The number of latent_features which can be changed based on the number of users
    Parameter: The learning rate
    Parameter: The epochs which essentially determines how long to learn for
    Return: Games-latent_features matrix
    Return: Latent_features-users matrix
    Return: The predicted users-games matrix without any empty elements for unplayed games for users
    """
    tf.compat.v1.disable_eager_execution() 
    game_user = tf.compat.v1.placeholder(tf.float32, shape=(num_games, num_users))

    # Initialising the game and user matrices using a Gaussian Distribution Randomizer
    game_matrix = tf.Variable(tf.random.normal([num_games, latent_features]))
    user_matrix = tf.Variable(tf.random.normal([latent_features, num_users]))

    predicteds = tf.matmul(game_matrix, user_matrix)

    # Loss Function
    loss = tf.reduce_mean(tf.square(game_user - predicteds))

    # Find minimum of loss function using Optimizer
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
    train_op = optimizer.minimize(loss)

    # Create the Tensorflow session so I can use sess instead of tf.compat.v1.Session()
    with tf.compat.v1.Session() as sess:
        # Initialize variables
        sess.run(tf.compat.v1.global_variables_initializer())

        # Training loop
        for epoch in range(epochs):
            _, l = sess.run([train_op, loss], feed_dict={game_user: user_game_matrix})

        # Get the learned game and user matrices
        main_game_matrix, main_user_matrix = sess.run([game_matrix, user_matrix])

        predicted_matrix = sess.run(predicteds, feed_dict={game_matrix: main_game_matrix, user_matrix: main_user_matrix})

        return main_game_matrix, main_user_matrix, predicted_matrix



def GetNRecommended(user_id, predicted_matrix, n):
    """
    Description: Get the n best games for a specific user
    Parameter: The user's id from the users database
    Parameter: The predicted users-games matrix
    Parameter: The number of games to recommend
    Return: The values of the top tensors
    Return: The corresponding indexes in arrays
    """
    wanted_row = (tf.compat.v1.matrix_transpose(predicted_matrix))[user_id]
    top_values, top_indices = tf.math.top_k(wanted_row, k=n, sorted=True)
    top_indices_arr = []
    for i in range(n):
        top_indices_arr.append(GetTensorValue(top_indices[i]))
    return top_values,top_indices_arr



def GetTensorValue(tensor_value):
    """
    Description: Gets the float tensor value of a tensor
    Parameter: The tensor value from a polars dataframe matrix
    Return: The float numerical value of a tensor
    """
    with tf.compat.v1.Session() as sess:
        return sess.run(tensor_value)
    


def GetUserRecommendations(genre_id, top_values, top_indices_arr, all_games):
    """
    Description: Gets the user's recommendations based on an array of the best recommended games for them and the genre that they want
    Parameter: genre_id has a one-to-one relationship with a specific genre in the games database
    Parameter: top_values is an array of the top tensor values
    Parameter: top_indices_arr is an array of the corresponding ids for the top tensor values
    Parameter: all_games is a list of all games in the games database
    Return: The 2D array of all recommended games along with their corresponding tensor values
    """
    connection = pymysql.connect(host='localhost', user='root', password='', database='games_db', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    game_dict_arr = []
    i=0
    for game_index in top_indices_arr:
        game_dict = all_games[game_index]
        game_id = game_dict["id"]
        if genre_id!=-1:
            cursor.execute(f"SELECT * FROM link_games_genres WHERE genre_id='{genre_id}' AND game_id='{game_id}'")
            game = cursor.fetchall()
            if game != ():
                tensor_value = GetTensorValue(top_values[i])
                game_dict_arr.append([game_dict, tensor_value])
        else:
            tensor_value = GetTensorValue(top_values[i])
            game_dict_arr.append([game_dict, tensor_value])
        i+=1
    cursor.close
    connection.close
    return game_dict_arr



def main(requesting_user_id, genre_id):
    """
    Description: Combines all of the functions in recommendations_processing.py
    Parameter: The user's id who is requesting for a recommendation
    Parameter: The id of the genre the user is requesting
    Return: The 2D array of all recommended games along with their corresponding tensor values
    """
    users = get_all_user_names()
    all_games = get_all_games()
    num_users = len(users)
    num_games = len(all_games)
    matrix_of_games_users = create_zero_matrix(num_games, num_users) # games will be the rows and users will be the columns
    #Now I have a matrix of games against users with each element of the matrix being 0.0 in float 64
    index_of_user = 0
    for user in users:
        user_name = user["user_name"]
        user_id,user_steam_id = get_user_ids(user_name)
        user_shortened_games_arr = user_processing(user_id, user_steam_id)
        matrix_of_games_users = filling_in_matrix(all_games, user_shortened_games_arr, matrix_of_games_users, index_of_user)
        index_of_user+=1
    matrix_of_games_users_pd = matrix_of_games_users.to_pandas()

    matrix_of_games_users_np = matrix_of_games_users.to_numpy()
    latent_features = 20
    learning_rate = 0.01
    epochs = 500
    game_matrix, user_matrix, predicted_matrix = matrix_factorization(matrix_of_games_users_np, num_users, num_games, latent_features, learning_rate, epochs)
    
    n = 50 # Number of recommendeds
    top_values,top_indices_arr = GetNRecommended(requesting_user_id, predicted_matrix, n)
    game_dict_arr = GetUserRecommendations(genre_id, top_values, top_indices_arr, all_games)
    return game_dict_arr
