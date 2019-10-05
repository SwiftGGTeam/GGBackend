class PageBean:

    def __init__(self, page: int, limit: int, total: int):
        self.page = page
        self.limit = limit
        self.total = total

    def to_json(self):
        return {
            'page': self.page,
            'size': self.limit,
            'total': self.total,
        }
