# QuestLink API

QuestLink API is a learning project that uses [Strawberry](https://strawberry.rocks/) as a GraphQL server and [SQLAlchemy](https://www.sqlalchemy.org/) as a database ORM. The project uses SQLite as the database for now.

The aim of this project is to have a bare-bone project setup that allows you to start writing GraphQL queries.

## Setup

1. **Install Python**
    To install using ds tools, use the following commands from dev shell
    
    ```sh
    ds tool install python3.11
    ```

2. **Create a virtual environment:**

    It is generally a good practice to create a virtual environment for your project, alternatively you can skip this process and install the requirements globally by going to step 4.
    You can create a virtual environment using the following command:

    ```sh
    python -m venv gql-env
    ```

3. **Activate the virtual environment:**

    On Windows:

    ```sh
    gql-env\Scripts\activate
    ```

    On Unix or MacOS:

    ```sh
    source gql-env/bin/activate
    ```

4. **Install the requirements:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Create the database:**

    ```sh
    alembic upgrade head
    ```

6. **Populating the database:**

I am using IGDB sample database that can be downloaded from the following Kaggle [link](https://www.kaggle.com/datasets/anudeepvanjavakam/igdb-api-data). You need a Kaggle account to download the dataset. Once you have downloaded the dataset, extract it to get a folder named `igdb_api_video_game_ratings_data`. 
Go to populate.py and set the value of CSV_DIR as full path of igdb_api_video_game_ratings_data folder.

    ```python
    CSV_DIR = Path("full path of igdb_api_video_game_ratings_data")
    ```

    Run the following command to populate the database:

    ```sh
    python populate.py
    ```

7. **Run the server:**

    The --reload flag automatically reloads the server when you make changes to the code.

    ```sh
    uvicorn app:app --reload
    ```


Now, you're ready to start writing GraphQL queries!

## Contributing

As this is a learning project, contributions are welcome. Feel free to open an issue or submit a pull request.

## License

This project is for learning purposes only and is not licensed for other use.