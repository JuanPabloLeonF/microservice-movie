class ModelMovie:

    def __init__(self, id: str, title: str, description: str, dateCreated: str, category: list[str], imgUrlCover: str, videoUrl: str):
        self.id: str = id
        self.title: str = title
        self.description: str = description
        self.dateCreated: str = dateCreated
        self.category: list[str] = category
        self.imgUrlCover: str = imgUrlCover
        self.videoUrl: str = videoUrl

    def getId(self) -> str:
        return self.id

    def setId(self, id: str) -> None:
        self.id = id

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

    def getImgUrlCover(self) -> str:
        return self.imgUrlCover

    def setImgUrlCover(self, imgUrlCover: str) -> None:
        self.imgUrlCover = imgUrlCover

    def getVideoUrl(self) -> str:
        return self.videoUrl

    def setVideoUrl(self, videoUrl: str) -> None:
        self.videoUrl = videoUrl

    def getJSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "dateCreated": self.dateCreated,
            "category": self.category,
            "imgFile": self.imgUrlCover,
            "videoFile": self.videoUrl
        }