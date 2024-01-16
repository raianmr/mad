# Running locally
Optionally create a virtual environment and activate it:
```
python3 -m venv .venv
.venv/Scripts/activate
```
Install dependencies:
```
python -m pip install -U pip  
pip install -U -r requirements.txt
```
## 20-MAD
```
cd MAD20
```
Create a database and `.env` file with the following:
```
DB_TYPE=postgresql+psycopg
DB_PORT=...
DB_USER=...
DB_PASS=...
DB_NAME=...
DB_HOST=localhost
```
To create the tables run:
```
alembic upgrade head
```
Inside `.env` add the following:
```
MAD20_LOCATION=data/osfstorage-archive/data/ [change if needed]
```

[//]: # (Preprocess the data &#40;makes a copy in `data/processed/`&#41;:)

[//]: # (```)

[//]: # (python scripts/preprocess.py)

[//]: # (```)
Load the data into the database:
```
python scripts/load_data.py
```