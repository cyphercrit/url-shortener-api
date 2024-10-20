# URL Shortener API
A URL Shortener REST API made with Flask and PostgreSQL, designed to be used with my personal website and deployed on Azure

## Prerequisites

- Python 3.7+
- A PostgreSQL Database

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/cyphercrit/url-shortener-api
cd url-shortener-api
```

### 2. Install the dependencies

```sh
pip install -r requirements.txt
```

### 3. Setup environment variables

```sh
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host/ip
DB_PORT=your_db_port
DB_NAME=your_db_name
```

### 5. Run the API

#### For Testing
```
python wsgi.py
```

#### For Production (Unix Only)
```sh
gunicorn -c gunicorn_config.py wsgi:app
```

## Testing the URL Shortener

### Shortening a URL
```sh
curl -X POST -H "Content-Type: application/json" -d "{\"url\": \"https://www.example.com\"}" http://127.0.0.1:5000/shorten
```

### Retrieving a short URL
```sh
curl -L http://127.0.0.1:5000/<short_url>
```

## License
This project is licensed under the MIT License.



