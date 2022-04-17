from fpdf import FPDF


class PDF(FPDF):
    width = 210
    height = 297

    def frame(self):
        self.set_fill_color(0.0, 0.0, 0.0)  # color for outer rectangle
        self.rect(5.0, 5.0, PDF.width - 10.0, PDF.height - 10.0, 'DF')
        self.set_fill_color(255, 255, 255)  # color for inner rectangle
        self.rect(10.0, 10.0, PDF.width - 20.0, PDF.height - 20.0, 'FD')

    def title(self, title):
        self.set_xy(10.0, 10.0)
        self.set_font('Arial', 'B', 42)
        self.set_text_color(220, 50, 50)
        self.cell(w=PDF.width-20.0, h=20.0, align='C', txt=title, border='TB')

    def subtitle(self, subtitle):
        self.set_xy(0.0, 30.0)
        self.set_font('Arial', 'BU', 36)
        self.set_text_color(220, 50, 50)
        self.cell(w=PDF.width, h=15.0, align='C', txt=subtitle, border=0)

    def insert_text(self, counter, text):
        q, r = divmod(counter, 4)
        x = 20.0 + 45.0 * r
        y = 50.0 + 100.0 * q
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.multi_cell(30, 5, text, align='C')

    def insert_image(self, counter, image):
        q, r = divmod(counter, 4)
        x = 20.0 + 45.0 * r
        y = 75.0 + 100.0 * q
        self.set_xy(x, y)
        self.image(image, link='', type='', w=1586/80, h=1920/80)
