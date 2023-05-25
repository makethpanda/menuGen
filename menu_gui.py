import sys
import json
import time
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QGridLayout,
    QPlainTextEdit,
    QFileDialog,
    QFormLayout,
    QScrollArea,
)

from main import main


class Beer(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.init_ui(data)

    def init_ui(self, data):
        layout = QVBoxLayout()

        # Title and separator line
        title = QLabel("Beer")
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Input widgets on the same row
        inputs_layout = QHBoxLayout()

        input_form_layout = QFormLayout()
        self.name = QLineEdit(data.get("name", ""))
        input_form_layout.addRow(QLabel("Name:"), self.name)

        self.price = QLineEdit(data.get("price", ""))
        input_form_layout.addRow(QLabel("Price:"), self.price)

        self.desc = QLineEdit(data.get("desc", ""))
        input_form_layout.addRow(QLabel("Desc:"), self.desc)

        inputs_layout.addLayout(input_form_layout)
        layout.addLayout(inputs_layout)

        self.setLayout(layout)


class Cocktail(QWidget):
    # Similar structure as Beer Class.
    def __init__(self, data=None):
        super().__init__()
        self.init_ui(data)

    def init_ui(self, data):
        layout = QVBoxLayout()

        # Title and separator line
        title = QLabel("Cocktail")
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Input widgets on the same row
        inputs_layout = QHBoxLayout()

        input_form_layout = QFormLayout()
        self.name = QLineEdit(data.get("name", ""))
        input_form_layout.addRow(QLabel("Name:"), self.name)

        self.price = QLineEdit(data.get("price", ""))
        input_form_layout.addRow(QLabel("Price:"), self.price)

        self.desc = QLineEdit(data.get("desc", ""))
        input_form_layout.addRow(QLabel("Desc:"), self.desc)

        inputs_layout.addLayout(input_form_layout)
        layout.addLayout(inputs_layout)

        self.setLayout(layout)


class Wine(QWidget):
    # Similar structure as Beer Class.
    def __init__(self, data=None):
        super().__init__()
        self.init_ui(data)

    def init_ui(self, data):
        layout = QVBoxLayout()

        # Title and separator line
        title = QLabel("Wine")
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Input widgets on the same row
        inputs_layout = QHBoxLayout()

        input_form_layout = QFormLayout()
        self.name = QLineEdit(data.get("name", ""))
        input_form_layout.addRow(QLabel("Name:"), self.name)

        self.price = QLineEdit(data.get("price", ""))
        input_form_layout.addRow(QLabel("Price:"), self.price)

        self.desc = QLineEdit(data.get("desc", ""))
        input_form_layout.addRow(QLabel("Desc:"), self.desc)

        inputs_layout.addLayout(input_form_layout)
        layout.addLayout(inputs_layout)

        self.setLayout(layout)


class Mocktail(QWidget):
    # Similar structure as Beer Class.
    def __init__(self, data=None):
        super().__init__()
        self.init_ui(data)

    def init_ui(self, data):
        layout = QVBoxLayout()

        # Title and separator line
        title = QLabel("Mocktail")
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Input widgets on the same row
        inputs_layout = QHBoxLayout()

        input_form_layout = QFormLayout()
        self.name = QLineEdit(data.get("name", ""))
        input_form_layout.addRow(QLabel("Name:"), self.name)

        self.price = QLineEdit(data.get("price", ""))
        input_form_layout.addRow(QLabel("Price:"), self.price)

        self.desc = QLineEdit(data.get("desc", ""))
        input_form_layout.addRow(QLabel("Desc:"), self.desc)

        inputs_layout.addLayout(input_form_layout)
        layout.addLayout(inputs_layout)

        self.setLayout(layout)


class MenuGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.beer_widgets = []
        self.cocktail_widgets = []
        self.wine_widgets = []
        self.mocktail_widgets = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Load and generate buttons
        self.load_button = QPushButton("Load JSON")
        self.generate_button = QPushButton("Generate Menu")
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.load_button)
        buttons_layout.addWidget(self.generate_button)
        layout.addLayout(buttons_layout)

        # Signals and slots
        self.load_button.clicked.connect(self.load_json)
        self.generate_button.clicked.connect(self.generate_menu)

        # Beer, Cocktail, Wine, Mocktail inputs
        beers_layout = QGridLayout()
        wines_layout = QGridLayout()
        cocktails_layout = QGridLayout()
        mocktails_layout = QGridLayout()

        with open("menu.json", "r") as file:
            data = json.load(file)

        for index, beer in enumerate(data["beers"]):
            beer_widget = Beer(beer)
            beers_layout.addWidget(beer_widget, 0, index)  # Row 0, and column as per the index
            self.beer_widgets.append(beer_widget)

        for index, cocktail in enumerate(data["cocktails"]):
            cocktail_widget = Cocktail(cocktail)
            cocktails_layout.addWidget(cocktail_widget, 0, index)
            self.cocktail_widgets.append(cocktail_widget)

        for index, wine in enumerate(data["wines"]):
            wine_widget = Wine(wine)
            wines_layout.addWidget(wine_widget, 0, index)
            self.wine_widgets.append(wine_widget)

        for index, mocktail in enumerate(data["mocktails"]):
            mocktail_widget = Mocktail(mocktail)
            mocktails_layout.addWidget(mocktail_widget, 0, index)
            self.mocktail_widgets.append(mocktail_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        scroll_layout.addLayout(beers_layout)
        scroll_layout.addLayout(wines_layout)
        scroll_layout.addLayout(cocktails_layout)
        scroll_layout.addLayout(mocktails_layout)

        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def load_json(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open JSON file", "", "JSON Files (*.json)")
        if file_name:
            with open(file_name, "r") as file:
                # Load JSON data and update the input fields
                self.json_input.setPlainText(file.read())

    def save_json(self):
        data = {
            "beers": [],
            "cocktails": [],
            "wines": [],
            "mocktails": [],
        }

        for beer_widget in self.beer_widgets:
            data["beers"].append({
                "name": beer_widget.name.text(),
                "price": beer_widget.price.text(),
                "desc": beer_widget.desc.text(),
            })

        for cocktail_widget in self.cocktail_widgets:
            data["cocktails"].append({
                "name": cocktail_widget.name.text(),
                "price": cocktail_widget.price.text(),
                "desc": cocktail_widget.desc.text(),
            })

        for wine_widget in self.wine_widgets:
            data["wines"].append({
                "name": wine_widget.name.text(),
                "price": wine_widget.price.text(),
                "desc": wine_widget.desc.text(),
            })

        for mocktail_widget in self.mocktail_widgets:
            data["mocktails"].append({
                "name": mocktail_widget.name.text(),
                "price": mocktail_widget.price.text(),
                "desc": mocktail_widget.desc.text(),
            })

        with open("menu.json", "w") as file:
            json.dump(data, file, indent=4)


    def generate_menu(self):
        self.save_json()
        main()
        img = Image.open('menu_output.png')
        img.show()


app = QApplication(sys.argv)
window = MenuGUI()
window.setWindowTitle("Menu Generator by MakethPanda")
window.show()
sys.exit(app.exec_())
