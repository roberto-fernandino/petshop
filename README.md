# Petshop Application

## Introduction

This application provides a platform to manage a pet shop's inventory and customer interactions. Follow the instructions below to set up and run the application on your local machine.

## Prerequisites

- Conda (Installation guide: [Install Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html))
- Python 3.11.4

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine.

### Step 2: Create a Conda Environment

Navigate to the project directory and create a Conda environment using the provided \`environment.yml\` file.

```bash
conda env create -f environment.yml
```

### Step 3: Activate the Conda Environment

Activate the Conda environment with the following command:

```bash
conda activate petshop
```

### Step 4: Apply Migrations

Apply the necessary database migrations:

#### Step 4.1:

Go to your src directory

#### Step 4.2:

Run
```bash
python manage.py makemigrations
```

#### Step 4.3:
```bash
python manage.py migrate
```

### Step 5: Start the Server

Run the application server:

```bash
python manage.py runserver
```

## Usage

The application is now running on your local server. Access it in your browser at [https://127.0.0.1:8000](https://127.0.0.1:8000).

For admin access, go to \`src/usuarios/conta_email.txt\` and use the provided account to log in at [https://127.0.0.1:8000/admin](https://127.0.0.1:8000/admin).

## Contributing

Feel free to contribute to this project by submitting issues, pull requests, or providing feedback.

## License

This project is licensed under the MIT License.


## Managing Products and Categories

### Automated Product Addition

This application allows for 100% automated addition of products through the admin panel. However, it's essential to note that product images must adhere to standardized sizes to maintain consistency across the application. Please ensure that all product images follow the required dimensions before uploading them.

### Managing Categories

Adding and modifying categories is a straightforward process in the admin panel. The interface is self-explanatory, allowing you to create, edit, or delete categories as needed. All category-related actions can be performed directly from the admin panel, providing a user-friendly experience.
