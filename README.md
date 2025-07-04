# Taquitos API

## Description
A Flask-based REST API for managing taquitos. This API allows users to perform CRUD (Create, Read, Update, Delete) operations on taquitos, which are stored in an SQLite database.

## API Endpoints

### 1. Get All Taquitos
- **Endpoint Path:** `/taquitos`
- **HTTP Method:** `GET`
- **Description:** Get all taquitos.
- **Response Body:**
  ```json
  [
    {"id": "<int>", "name": "<string>", "rate": "<int>", "image": "<string_url>"},
    ...
  ]
  ```

### 2. Create a New Taquito
- **Endpoint Path:** `/taquitos`
- **HTTP Method:** `POST`
- **Description:** Create a new Taquito.
- **Request Body:**
  ```json
  {"name": "<string>", "rate": "<int>", "image": "<string_url>"}
  ```
- **Response Body:** (confirms the created taquito)
  ```json
  {"name": "<string>", "rate": "<int>", "image": "<string_url>"}
  ```

### 3. Update an Existing Taquito
- **Endpoint Path:** `/taquitos/update`
- **HTTP Method:** `PUT`
- **Description:** Update an existing Taquito.
- **Request Body:**
  ```json
  {"id": "<int>", "name": "<string>", "rate": "<int>", "image": "<string_url>"}
  ```
- **Response Body:**
  ```json
  {"msg": "Updated successfully"}
  ```

### 4. Delete a Taquito
- **Endpoint Path:** `/taquitos/<id>`
- **HTTP Method:** `DELETE`
- **Description:** Delete a Taquito by its ID.
- **Response Body:**
  ```json
  true
  ```

### 5. Get a Specific Taquito
- **Endpoint Path:** `/taquitos/<id>`
- **HTTP Method:** `GET`
- **Description:** Get a specific taquito by its ID.
- **Response Body:**
  ```json
  {
    "msg": "listed one taquito",
    "data": {
      "id": "<int>",
      "name": "<string>",
      "rate": "<int>",
      "image": "<string_url>"
    }
  }
  ```

### 6. Count Taquitos
- **Endpoint Path:** `/taquitos/count`
- **HTTP Method:** `GET`
- **Description:** Count how many taquitos exist.
- **Response Body:**
  ```json
  <int>
  ```

## Database Schema

**Table: `taquitos`**

| Column | Data Type | Constraints        | Description                  |
|--------|-----------|--------------------|------------------------------|
| id     | INTEGER   | NOT NULL, UNIQUE, PRIMARY KEY AUTOINCREMENT | Unique identifier for the taquito |
| name   | TEXT      | NOT NULL           | Name of the taquito          |
| rate   | INTEGER   | NOT NULL, DEFAULT 5 | Rating of the taquito (1-5)  |
| image  | TEXT      | UNIQUE             | URL or path to an image of the taquito |

## Setup and Running Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    *(Replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name)*

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.text
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory of the project with the following content:
    ```env
    SECRET_KEY='your_secret_key_here'
    DATABASE_NAME='taquitos.db' 
    ```
    Replace `'your_secret_key_here'` with an actual secret key. `DATABASE_NAME` can be kept as `taquitos.db` or changed if needed.
    *Note: The application relies on `python-dotenv` to load these variables from the `.env` file as seen in `settings.py`.*

5.  **Initialize the database (if running for the first time):**
    The application creates the database and tables automatically when it starts. This is handled by the `create_tables()` function in `db.py`, which is called when `api.py` is executed.

6.  **Run the application:**
    ```bash
    python api.py
    ```
    The API will then be accessible at `http://0.0.0.0:8000` or `http://localhost:8000`.

## Dependencies

The project relies on the following Python packages:

```
click==8.0.1
colorama==0.4.4
Flask==2.0.1
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
python-decouple==3.4
Werkzeug==2.0.1
yapf==0.31.0
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or find any bugs.
