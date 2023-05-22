# PlantUrbanus: Server

PlantUrbanus is a fullstack app for managing houseplants. This is the backend, a FastAPI / MongoDB / REST server. Abstractly speaking it can be seen as the foundation for any app that uses MongoDB as a database with two types of document models: User and Plant (or Product, or Book, or Item).

In this server User is authenticated with JWT and Plant is associated with a corresponding User. That is, User can have multiple Plant(s), and each Plant has a field indicating which User owns the Plant.

## Using this repository to scaffold your own app

In addition to installing a python virtual environment (I used version 3.11), you'll need to create an .env file (you can .sample_env as a point of departure) to hold the following private values:

- CLOUDINARY_URL: All User-specific images of Plant(s) are saved in Cloudinary, so you will need your own url here. CLOUD_NAME, API_KEY, API_SECRET may be superfluous.
- MONGO_URI, MONGO_DB: Your connection to the database will need the first, and your functions to connect to the specific documents in the database will need to explicitly name the database, or you can reference MONGO_DB for added security.
- SECRET_KEY, ALGORITHM: These are needed for User authentication. The first is a randomly created string for security purposes and the second is the decryption algorithm, for example, HS256.

The file requirements.txt should have all the additional install you will need. Use `pip install -r requirements.txt` to install

## Launching the app

If you have copied my main.py file, you can launch the server using:

```terminal
python3 main.py
```

Alternatively, FastAPI servers are traditionally launched using:

```terminal
uvicorn main:app --reload
```

## Further notes

I will be explaining the authentication method in a series of blog posts that I am in the process of writing as of May 2023. Please see [el-cordovez.com](https://www.el-cordovez.com).

The front-end part of this app can be found here: [PlantUrbanus_client_v4](https://github.com/cordovez/PlantUrbanus_client_v4)
