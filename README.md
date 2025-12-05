# Bank Branch API Service

## Description
This project is a REST API server for banks and branches data. Built with Django and Django REST Framework (DRF), it provides endpoints to list banks, list branches, and search for branches by IFSC code. 

## 🚀 Project Setup and Execution

### Prerequisites

* Python (3.8+)
* Django (A compatible version, generally 4.x or newer)
* Django REST Framework
* PostgreSQL (or another database configured in `settings.py`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SaurabhSB07/bank_api](https://github.com/SaurabhSB07/bank_api)
    cd bank_api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install django djangorestframework psycopg2-binary 
    ```

4.  **Database Configuration:**
    Ensure your PostgreSQL database is running and the connection details in `bank_api/settings.py` are correct:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bank_db', 
            'USER': 'postgres',
            'PASSWORD': '123',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5.  **Run Migrations:**
    ```bash
    python manage.py makemigrations core
    python manage.py migrate
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

---

## 💻 REST API Endpoints

The core business logic is implemented in the **`core`** application, providing the following endpoints:

| Endpoint URL | HTTP Method | Description | Assignment Requirement |
| :--- | :--- | :--- | :--- |
| `/api/banks/` | `GET` | **Bank List:** Returns a list of all banks. | *Bank List* |
| `/api/branches/` | `GET` | Returns a list of all bank branches. | (Supporting Endpoint) |
| `/api/branches/search/` | `GET` | **Branch Details:** Supports filtering by **IFSC** code. | *Branch details for a specific branch* |

### Search Endpoint Usage

The `/api/branches/search/` endpoint is the designated method for retrieving specific branch details.

* **Query by IFSC:**
    ```
    /api/branches/search/?ifsc=<IFSC_CODE>
    ```
    *Example: `/api/branches/search/?ifsc=TEST0001`*

---

## 📐 Implementation Details

### Technology Stack
* **Backend Framework:** Django
* **API Framework:** Django REST Framework (DRF)
* **Database:** PostgreSQL (configured)

### Key Decisions

1.  **Read-Only Operations:** All API views use `generics.ListAPIView` as the requirement is only to *get* data (list banks, search branches).
2.  **Nested Serialization:** The `BranchSerializer` includes the `BankSerializer` for the `bank` field:
    ```python
    bank = BankSerializer(read_only=True)
    ```
    This ensures that when querying a branch, the response includes the complete details of the associated bank, satisfying the requirement for "its branch details."
3.  **Search Logic:** The `BranchSearchAPIView` overrides the `get_queryset` method to filter the results dynamically based on the **`ifsc`** query parameter, providing a specific branch lookup mechanism.

---

## ✅ Test Cases (Bonus Points)

Unit tests are included in **`core/tests.py`** to cover the core functionality:

* **`test_bank_list_endpoint`**: Verifies that the bank list endpoint returns the correct status code and number of objects.
* **`test_branch_list_endpoint`**: Verifies the list of all branches.
* **`test_branch_search_endpoint`**: Verifies the specific search functionality using the `ifsc` query parameter.

---

## ⏱️ Time Taken to Complete the Assignment

**Total Time: Approximately 3 hours**

| Task | Estimated Time |
| :--- | :--- |
| Environment Setup, DB & Project Structure | 30 minutes |
| Models, Serializers, Views, and URLs Implementation | 75 minutes |
| Writing Unit Tests | 60 minutes |
| Documentation (README) | 15 minutes |

