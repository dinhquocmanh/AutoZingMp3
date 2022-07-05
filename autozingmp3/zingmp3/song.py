
class Song:
    """
    Class Song:
        Object Song = bài hát. 
        vd: tạo bài hát mới thì tạo một instance Song mới
        sau đó truyền vào các tham số của bài hát.
        Khi cần lấy các thông tin bài hát ra thì chỉ cần 
        truy cập vào các attributes của bài hát 
    """   
    def __init__(self, name: str, author: str, length: str, 
            created_date: str, trending: bool, url: str) -> None:
        self.name = name 
        self.author = author
        self.length = length 
        self.created_date = created_date
        self.trending = trending 
        self.url = url 