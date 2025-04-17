import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def create_movies_table():
    try:
        table = dynamodb.create_table(
            TableName='MoviesWithGenres',
            KeySchema=[
                {
                    'AttributeName': 'movie_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'movie_id',
                    'AttributeType': 'S'  # 'S' for string
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        print("Creating table...")
        table.wait_until_exists()
        print("✅ Table created and ready!")
        return table

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("ℹ️ Table already exists.")
            return dynamodb.Table('MoviesWithGenres')
        else:
            raise

def add_movie(movie_id, title, genres):
    table = dynamodb.Table('MoviesWithGenres')
    item = {
        'movie_id': movie_id,
        'title': title,
        'genres': genres
    }
    table.put_item(Item=item)
    print(f"✅ Added: {title}")
def add_movies():
    movies = [
        {'movie_id': '1', 'title': 'The Matrix', 'genres': ['Action', 'Sci-Fi']},
        {'movie_id': '2', 'title': 'Pride & Prejudice', 'genres': ['Romance', 'Drama']},
        {'movie_id': '3', 'title': 'Shrek', 'genres': ['Animation', 'Comedy']}
    ]

    for movie in movies:
        add_movie(movie['movie_id'], movie['title'], movie['genres'])


if __name__ == '__main__':
    create_movies_table()
    add_movies()
