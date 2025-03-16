# Installing a Python Project

## Prerequisites
Ensure you have the following installed on your system:
- [Python](https://www.python.org/downloads/) (3.x recommended)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Installation Steps

### 1. Clone the Repository
Use `git` to clone the project repository:

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment

#### Using Windows
```
python -m venv venv
venv\Scripts\activate
```

#### Using Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependecies
```
pip install -r requirements.txt
```

### 4.  Run the Project

### 5. Deactivate The VENV
```
deactivate
```