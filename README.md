# Catalogue API

<<<<<<< HEAD
A small FastAPI tutorial project that demonstrates routing, path and query parameters,
Pydantic request and response models, enums, and HTTP methods.

The current implementation lives in `tutorial.py` and uses an in-memory item list.
It does not connect to PostgreSQL or Supabase yet.

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

Using uv:

```bash
uv sync
```

Using pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the API

From the project directory, run:

```bash
uv run fastapi dev tutorial.py
```

The API is available at <http://127.0.0.1:8000>. Interactive documentation is
available at:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## Example endpoints

=======
A small FastAPI tutorial project demonstrating routing, path and query parameters,
Pydantic request and response models, enums, response filtering, and redirects.

The application is defined in `tutorial.py`. Its example data is stored in memory;
it does not connect to PostgreSQL or Supabase, and its signup and login routes do not
implement authentication.

## Requirements

- Python 3.11 or newer

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, use this activation command instead:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the API

From the project directory, run:

```bash
fastapi dev tutorial.py
```

The API is available at <http://127.0.0.1:8000>. Interactive documentation is
available at:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## Example endpoints

>>>>>>> 5744fb65077dd35af37d3f96e87813415c3eff5e
| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message |
| `POST` | `/signup` | Returns a signup confirmation |
| `PUT` | `/login` | Returns a login confirmation |
| `DELETE` | `/login` | Returns a deletion confirmation |
| `GET` | `/users` | Returns a list of example users |
| `GET` | `/users/me` | Returns the current-user placeholder |
| `GET` | `/users/{userid}` | Returns a numeric user ID |
| `GET` | `/models/{model_name}` | Returns a message for `alexnet`, `resnet`, or `lenet` |
<<<<<<< HEAD
| `GET` | `/items?skip=0&limit=10` | Returns a paginated slice of the in-memory item list |
| `GET` | `/files/{file_path}` | Returns an example file path; supports nested paths |
| `POST` | `/items` | Creates an item from a Pydantic request body |
| `PUT` | `/items/{item_id}` | Updates an item and optionally accepts a `q` query parameter |
| `GET` | `/items/{item_id}` | Returns the sample item response list |
=======
| `GET` | `/items?skip=0&limit=10` | Returns a paginated slice of the in-memory example list |
| `GET` | `/files/{file_path}` | Echoes a file path; supports nested paths |
| `POST` | `/items` | Validates an item and returns it with `price_with_tax` when tax is provided |
| `GET` | `/items/{item_id}` | Returns a sample item (`foo`, `bar`, or `baz`); omits unset fields |
| `POST` | `/client` | Validates client details and returns the client without the password |
| `GET` | `/portal?teleport=true` | Redirects to an external URL when `teleport` is true; otherwise returns a message |
| `GET` | `/teleport` | Redirects to an external URL |
>>>>>>> 5744fb65077dd35af37d3f96e87813415c3eff5e

## Example requests

Create an item:

```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name":"Portal Gun","description":"Portal device","price":42,"tax":5}'
```

Get a model:

```bash
curl "http://127.0.0.1:8000/models/alexnet"
```

Get a page of items:

```bash
curl "http://127.0.0.1:8000/items?skip=0&limit=2"
```
<<<<<<< HEAD
=======

Create a client (the response excludes the password):

```bash
curl -X POST "http://127.0.0.1:8000/client" \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada","email":"ada@example.com","password":"example-password"}'
```

Get one of the sample items:

```bash
curl "http://127.0.0.1:8000/items/foo"
```
>>>>>>> 5744fb65077dd35af37d3f96e87813415c3eff5e

