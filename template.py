import os
from pathlib import Path

from setup import PROJECT_NAME

list_of_files = [
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_cleaning.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/constants/__init__.py",
    f"{PROJECT_NAME}/data_access/__init__.py",
    f"{PROJECT_NAME}/data_access/{PROJECT_NAME}_data.py",
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",
    f"{PROJECT_NAME}/entity/estimator.py",
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/logger/__init__.py",
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/utils/main_utils.py",
    "notebook/1_EDA_and_Visualization.ipynb",
    "notebook/2_Data_Preprocessing_and_Feature_Engineering.ipynb",
    "notebook/3_Model_Training_and_Model_Evaluation.ipynb",
    f"templates/{PROJECT_NAME}.html",
    "static/css/style.css",
    "app.py",
    "requirements.txt",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File is already present at: {filepath}")
