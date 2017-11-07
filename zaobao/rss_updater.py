from zaobao import Zaobao
import sys, os

class RssUpdater:
    def __init__(self):
        self.zb = Zaobao()
        self.last_url = ""
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.last_url_file_path = os.path.join(self.dir, "zaobao_last_url.txt")
        self.rss_xml_file_path = os.path.join(self.dir, "zaobao_rss.xml")

    def update(self):
        if os.path.exists(self.last_url_file_path):
            file = open(f)
            self.last_url = file.read().strip()

        fetch_end = False
        page = 1
        while fetch_end != True:
            print "fetching...."
            self.zb.main(page)
            if self.fetch_finished():
                fetch_end = True
            page += 1
        self.zb.generate(self.rss_xml_file_path)
        self.update_last_url()

    def fetch_finished(self):
        print self.last_url
        print self.zb.size()
        if len(self.last_url) <= 0 and self.zb.size() >= 50:
            return True
        elif self.zb.size() >= 50 and self.zb.contains_item_by_url(self.last_url):
            return True
        else:
            return False
        
    def update_last_url(self):
        file = open(self.last_url_file_path, "w")
        file.write(self.zb.first_url())

if __name__ == "__main__":
    RssUpdater().update()


