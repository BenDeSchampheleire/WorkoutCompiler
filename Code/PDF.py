from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os.path


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
        self.cell(w=PDF.width - 20.0, h=20.0, align='C', txt=title, border='TB')

    def subtitle(self, subtitle):
        self.set_xy(0.0, 30.0)
        self.set_font('Arial', 'BU', 28)
        self.set_text_color(220, 50, 50)
        self.cell(w=PDF.width, h=15.0, align='C', txt=subtitle, border=0)

    def insert_exercise_name(self, counter, text):
        q, r = divmod(counter, 4)
        x = 20.0 + 45.0 * r
        y = 50.0 + 100.0 * q
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        self.multi_cell(30.0, 5.0, text.title(), align='C')

    def search_exercise_image(self, exercise_name):
        base_URL = "https://www.bodybuilding.com/exercises/"
        dynamic_URL = "search?query=" + exercise_name.replace(" ", "+")

        page = requests.get(base_URL + dynamic_URL)  # retrieve the html page
        soup = BeautifulSoup(page.content, "html.parser")  # parse the html page
        images = soup.find_all("img", alt=" thumbnail image")  # find all thumbnails on the html page
        titles = soup.find_all("h3")  # find all Headers3 on the html page
        try:
            first_image = images[0]  # select the first thumbnail
            first_name = titles[0].find("a").text.strip()  # extract the name of the first Header3
            return [first_name, first_image["data-src"]]  # return the URL of this thumbnail and the name
        except IndexError:
            print("No match was found in the online database")
            return False

    def get_image(self, image_attributes):
        if image_attributes != False:
            image_name = image_attributes[0]
            image_URL = image_attributes[1]
            file = "Resources/Database/" + image_name.replace(" ", "_") + ".png"
            if os.path.exists(file):
                return file
            else:
                response = requests.get(image_URL)
                image = Image.open(BytesIO(response.content))
                image.save(file)
                return file
        else:
            return False

    def insert_exercise_image(self, counter, image):
        q, r = divmod(counter, 4)
        x = 20.0 + 45.0 * r
        y = 60.0 + 100.0 * q
        if image != False:
            self.set_xy(x-5.0, y)
            self.image(image, link='', type='', w=40.0, h=60.0)
        else:
            self.set_xy(x, y+30.0)
            self.multi_cell(30.0, 5.0, "No search results", align='C')

    def insert_exercise_specs(self, counter, exercise):
        q, r = divmod(counter, 4)
        x = 20.0 + 45.0 * r
        y = 125.0 + 100.0 * q
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 12)
        text = "Reps: %d \n Sets: %d \n Rest: %d" % (exercise.reps, exercise.sets, exercise.rest)
        self.multi_cell(30.0, 5.0, text, align='C')
