import os

project_name = "fake-news-detection"

folders = [
    ".github/workflows",
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "src/components",
    "src/pipeline",
    "src/configuration",
    "src/constant",
    "src/entity",
    "src/utils",
    "config",
    "artifacts",
    "templates",
    "static",
    "prediction_test_file",
    "tests",
    "logs",
    "mlruns"
]

files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/pipeline/__init__.py",
    "src/configuration/__init__.py",
    "src/constant/__init__.py",
    "src/entity/__init__.py",
    "src/utils/__init__.py",
    "config/__init__.py",
    "tests/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "app.py",
    "main.py",
    "dvc.yaml",
    "params.yaml",
    "Dockerfile",
    "docker-compose.yml",
    ".dockerignore",
    ".gitignore",
    ".dvcignore",
    "requirements.txt",
    "requirements-dev.txt",
    "setup.py",
    "config/config.yaml",
    "README.md"
]

for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

for file in files:
    file_path = os.path.join(project_name, file)
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass

print("Project structure created successfully.")
