import zaobao

class RssUpdater:
    def __init__(self):
        return

    def update(self):
        file = open("zaobao_last_url.txt")
        url = file.read().strip()

