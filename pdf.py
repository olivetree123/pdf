#coding:utf8


class MediaBox(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def __str__(self):
        return "[{} {} {} {}]".format(self.x, self.y, self.w, self.h)

    def text(self):
        return str(self)


class PDFObject(object):
    Type = None

    def __init__(obj_id,
                 parent_id=None,
                 kids=None,
                 content=None,
                 media_box: MediaBox = None):
        if not isinstance(kids, (list, tuple)):
            raise TypeError("kids should be type of list, but {} found".format(
                type(kids)))
        if not isinstance(media_box, MediaBox):
            raise TypeError(
                "media_box should be type of MediaBox, but {} found".format(
                    type(media_box)))
        self.obj_id = obj_id
        self.type = Type
        self.parent_id = parent_id
        self.kids = kids if kids else []
        self.media_box = media_box

    def text(self):
        start_line = "{OBJ_ID} 0 obj \n << \n".format(OBJ_ID=self.obj_id)
        end_line = "\n >> \n endobj \n"
        content = "/Type {TYPE} \n /Count {COUNT} \n "
        # 如果有父对象
        if self.parent_id:
            content += "/Parent {PARENT_ID} 0 R \n".format(
                PARENT_ID=self.parent_id)
        # 如果有子对象
        if self.kids:
            kids_list = []
            for kid in self.kids:
                kids_list.append(kid)
                kids_list.append(0)
                kids_list.append("R")
            if kids_list:
                content += "/Kids " + str(kids_list) + "\n"
        if self.media_box:
            content += "/MediaBox {} \n".format(self.media_box.text())
        return start_line + content + end_line


class CatalogObject(PDFObject):
    Type = "Catalog"


class OutLineObject(PDFObject):
    Type = "Outlines"


class PagesObject(PDFObject):
    Type = "Pages"


class PageObject(PDFObject):
    Type = "Page"


class Page(object):
    def __init__(self):
        self.content = ""


class PDF(object):
    def __init__(self, out_file):
        self.header = "%PDF-1.5"
        self.out_file = out_file
        self._pages = []
        self._page = None  # 当前 page
        self.obj_id = 1  # 当前对象 id

    def AddPage(self):
        self._page = Page()
        self._pages.append(self._page)

    def Text(self, text):
        pass

    def BookMark(self):
        self._page.content += ""
        pass

    def _write_header(self):
        pass

    def _write_text(self, text):
        pass

    def Save(self):
        with open(self.out_file, "wb") as f:
            f.write()


pdf = PDF("test.pdf")
pdf.AddPage()
pdf.Text("Hello PDF")
pdf.Save()