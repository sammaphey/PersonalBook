# PersonalBook Library Management

Welcome to PersonalBook!

To get started follow the [Start-Up](#startup) instructions/

## Startup

### API

#### Pre-requisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/)

#### API Dependency Installation

- run `poetry install`
- Launch the application `api launch`

#### Env File

- Add a new `.env` file in the `api` directory with the following form:

```env
BOOK_API_SECRET=this_is_a_fake_secret
BOOK_ORIGINS=["http://localhost:4200"]
BOOK_PORT=5002

BOOK_MONGO_USERNAME=your-username
BOOK_MONGO_PASSWORD=your-password
BOOK_MONGO="mongo-db-uri"
BOOK_MONGO_DB_NAME=mongodb-name
```

Being sure to replace tha values of `BOOK_MONGO_USERNAME`, `BOOK_MONGO_PASSWORD`, `BOOK_MONGO`, and `BOOK_MONGO_DB_NAME` with the appropriate values for your setup.
