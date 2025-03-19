import json
from datetime import datetime
from fastapi import Form, UploadFile, File

class MovieRequestForm:
    def __init__(
        self,
        title: str = Form(min_length=3, max_length=200),
        description: str = Form(min_length=5, max_length=400),
        dateCreation: str = Form(min_length=10, max_length=20),
        category: str = Form(),
        imgFile: UploadFile = File(),
        videoFile: UploadFile = File(),
    ):
        self.title = title
        self.description = description
        self.dateCreation = MovieRequestForm.validateDateCreation(value=dateCreation)
        self.category = MovieRequestForm.validateCategory(value=category)
        self.imgFile = imgFile
        self.videoFile = videoFile

    @staticmethod
    def validateCategory(value: str) -> list[str]:
        try:
            data: list[str] = json.loads(value)

            if not isinstance(data, list):
                raise ValueError("category debe ser una lista de strings")

            if len(data) == 0:
                raise ValueError("category debe tener al menos un elemento")

            for item in data:
                if not isinstance(item, str) or item.strip() == "":
                    raise ValueError("category no puede estar vacio")

            return data
        except (ValueError, json.JSONDecodeError):
            raise ValueError("category must be a list of strings")

    @staticmethod
    def validateDateCreation(value: str) -> str:
        try:
            datetime.strptime(value, "%d/%m/%Y")
            return value
        except ValueError:
            raise ValueError("dateCreation must be in DD/MM/YYYY")

    def getJSON(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "dateCreation": self.dateCreation,
            "category": self.category,
            "imgFile": self.imgFile.filename,
            "videoFile": self.videoFile.filename
        }
