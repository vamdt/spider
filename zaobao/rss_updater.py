from zaobao import Zaobao

class RssUpdater:
    def __init__(self):
        self.zb = Zaobao()
        self.last_url = ""
        return

    def update(self):
        file = open("zaobao_last_url.txt")
        self.last_url = file.read().strip()
        fetch_end = False
        page = 1
        while fetch_end != True:
            self.zb.main(page)
            if fetch_finished():
                fetch_end = True
            page += 1
        self.zb.generate()
        update_last_url()

    def fetch_finished():
        if len(self.last_url) <= 0 && self.zb.size() > = 50:
            return True
        else if self.zb.size() >= 50 && self.zb.contains_item_by_url(url):
            return True
        else:
            return False
        
    def update_last_url():
        file = open("zaobao_last_url_txt", "w")
        file.write(self.zb.first_url())


