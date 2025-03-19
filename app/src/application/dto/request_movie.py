from fastapi import UploadFile

class MovieRequest:

    def __init__(self, title: str, description: str, dateCreated: str, category: list[str], imgFile: UploadFile, videoFile: UploadFile):
        self.title: str = title
        self.description: str = description
        self.dateCreated: str = dateCreated
        self.category: list[str] = category
        self.imgFile: UploadFile = imgFile
        self.videoFile: UploadFile = videoFile

    def getTitle(self) -> str:
        return self.title

    def setTitle(self, title: str) -> None:
        self.title = title

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description: str) -> None:
        self.description = description

    def getDateCreated(self) -> str:
        return self.dateCreated

    def setDateCreated(self, dateCreated: str) -> None:
        self.dateCreated = dateCreated

    def getCategory(self) -> list[str]:
        return self.category

    def setCategory(self, category: list[str]) -> None:
        self.category = category

    def getImgFile(self) -> UploadFile:
        return self.imgFile

    def setImgFile(self, imgUrlFile: UploadFile) -> None:
        self.imgFile = imgUrlFile

    def getVideoFile(self) -> UploadFile:
        return self.videoFile

    def setVideoFile(self, videoFile: UploadFile) -> None:
        self.videoFile = videoFile

    def getJSON(self):
        return {
            "title": self.title,
            "description": self.description,
            "dateCreated": self.dateCreated,
            "category": self.category,
            "imgFile": self.imgFile,
            "videoFile": self.videoFile
        }