import xml.etree.cElementTree as ET

class Channel:
    def __init__(self):
        self.title = ""
        self.link = ""
        self.description = ""
        self.image_url = ""
        self.language = ""
        self.copyright = ""
        self.ttl = 60
        self.last_build_date = ""
        self.generator = ""

class ChannelItem:
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        self.comments=""
        self.pub_date = ""
        self.categories = []
        self.guid = link
        self.author = ""

class RssBuilder:
    def __init__(self):
        self.rss = ET.Element("rss")
        self.rss.attrib = {"version": "2.0", "xmlns:atom": "http://www.w3.org/2005/Atom"}


    def build(self, channel, channel_item_list):
        self.build_channel(channel)
        self.build_items(channel_item_list)
        self.build_end()

    def build_channel(self, channel):
        self.channel_el = ET.SubElement(self.rss, "channel")
        ET.SubElement(self.channel_el, "title").text = channel.title
        ET.SubElement(self.channel_el, "link").text = channel.link
        ET.SubElement(self.channel_el, "description").text = channel.description
        ET.SubElement(self.channel_el, "lastBuildDate").text = channel.last_build_date
        ET.SubElement(self.channel_el, "language").text = channel.language
        ET.SubElement(self.channel_el, "atom:link").attrib = {"href": channel.link, "rel": "self", "type": "application/rss+xml"}
        image_el = ET.SubElement(self.channel_el, "image")
        ET.SubElement(image_el, "url").text = channel.image_url
        ET.SubElement(image_el, "title").text = channel.title
        ET.SubElement(image_el, "link").text = channel.link


    def build_items(self, channel_item_list):
        for channel_item in channel_item_list:
            self.build_item(channel_item)

    def build_item(self, channel_item):
        channel_item_el = ET.SubElement(self.channel_el, "item")
        ET.SubElement(channel_item_el, "title").text = channel_item.title
        ET.SubElement(channel_item_el, "link").text = channel_item.link
        ET.SubElement(channel_item_el, "author").text = channel_item.author
        ET.SubElement(channel_item_el, "pubDate").text = channel_item.pub_date
        ET.SubElement(channel_item_el, "guid").text = channel_item.guid
        ET.SubElement(channel_item_el, "description").text = channel_item.description
        for category in channel_item.categories:
            ET.SubElement(channel_item_el, "category").text = category

    def build_end(self):
        self.tree =  ET.ElementTree(self.rss)

    def write(self, file_path):
        self.tree.write(file_path, "utf-8")






