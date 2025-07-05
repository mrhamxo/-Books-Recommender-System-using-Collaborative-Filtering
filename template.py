import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


project_name = "books_recommendation"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/1_data_ingestion.py",
    f"{project_name}/components/2_data_validation.py",
    f"{project_name}/components/3_data_transformation.py",
    f"{project_name}/components/4_model_trainer.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception_handler.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/log.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/util.py",
    "config/config.yaml",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "setup.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    
    file_dir = file_path.parent
    if not file_dir.exists():
        logging.info(f"Creating directory: {file_dir}")
        os.makedirs(file_dir, exist_ok=True)
    
    if not file_path.exists():
        logging.info(f"Creating file: {file_path}")
        with open(file_path, 'w') as f:
            pass  # Create an empty file
    else:
        logging.info(f"File already exists: {file_path}")