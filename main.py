import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import json
import yaml
import xml.etree.ElementTree as xml

class FileLoaderThread(QThread):
    data_loaded = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, input_file):
        super().__init__()
        self.input_file = input_file

    def run(self):
        try:
            if self.input_file.endswith('.json'):
                data = load_json(self.input_file)
            elif self.input_file.endswith('.yaml'):
                data = load_yaml(self.input_file)
            elif self.input_file.endswith('.xml'):
                data = load_xml(self.input_file)
            else:
                self.error.emit("Nieobsługiwany format pliku wejściowego.")
                return
            self.data_loaded.emit(data)
        except Exception as e:
            self.error.emit(str(e))

class FileSaverThread(QThread):
    success = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, data, output_file, output_format):
        super().__init__()
        self.data = data
        self.output_file = output_file
        self.output_format = output_format

    def run(self):
        try:
            if self.output_format == 'json':
                if isinstance(self.data, xml.Element):
                    data_dict = _xml_to_dict(self.data)
                    save_json(data_dict, self.output_file)
                else:
                    save_json(self.data, self.output_file)
            elif self.output_format == 'yaml':
                save_yaml(self.data, self.output_file)
            elif self.output_format == 'xml':
                root = xml.Element("data")
                _convert_to_xml_recursive(self.data, root)
                save_xml(root, self.output_file)
            else:
                self.error.emit("Nieobsługiwany format pliku wyjściowego.")
                return
            self.success.emit(f"Dane zostały zapisane do pliku {self.output_file}")
        except Exception as e:
            self.error.emit(str(e))

def load_json(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)

def save_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml(input_file):
    with open(input_file, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def load_xml(input_file):
    tree = xml.parse(input_file)
    return tree.getroot()

def save_xml(data, output_file):
    with open(output_file, 'w') as file:
        xml_string = xml.tostring(data).decode()
        file.write(xml_string)

def _convert_to_xml_recursive(data, parent):
    if isinstance(data, dict):
        for key, value in data.items():
            element = xml.SubElement(parent, key)
            _convert_to_xml_recursive(value, element)
    elif isinstance(data, list):
        for item in data:
            _convert_to_xml_recursive(item, parent)
    else:
        parent.text = str(data)

def _xml_to_dict(element):
    def _parse_element(element):
        parsed = {}
        for child in element:
            if len(child):
                if child.tag in parsed:
                    if isinstance(parsed[child.tag], list):
                        parsed[child.tag].append(_parse_element(child))
                    else:
                        parsed[child.tag] = [parsed[child.tag], _parse_element(child)]
                else:
                    parsed[child.tag] = _parse_element(child)
            else:
                if child.tag in parsed:
                    if isinstance(parsed[child.tag], list):
                        parsed[child.tag].append(child.text)
                    else:
                        parsed[child.tag] = [parsed[child.tag], child.text]
                else:
                    parsed[child.tag] = child.text
        return parsed

    return {element.tag: _parse_element(element)}

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.init_ui()
        self.data = None

    def init_ui(self):
        self.setWindowTitle("File Converter")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #151515")

        layout = QVBoxLayout(self)
        
        self.input_label = QLabel("Input File:", self)
        self.input_label.setStyleSheet("color: #EEEEEE; font-size: 16px; font-weight: bold; font-family: sans-serif;")
        layout.addWidget(self.input_label)

        self.input_button = QPushButton("Select Input File", self)
        self.input_button.setStyleSheet("color: #EEEEEE; border: 2px solid #A91D3A; border-radius: 8px; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; font-family: sans-serif;")
        self.input_button.clicked.connect(self.select_input_file)
        layout.addWidget(self.input_button)

        self.output_label = QLabel("Output File:", self)
        self.output_label.setStyleSheet("color: #EEEEEE; font-size: 16px; font-weight: bold; font-family: sans-serif;")
        layout.addWidget(self.output_label)

        self.json_button = QPushButton("JSON", self)
        self.json_button.setStyleSheet("color: #EEEEEE; border: 2px solid #A91D3A; border-radius: 8px; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; font-family: sans-serif;")
        self.json_button.clicked.connect(lambda: self.select_output_format("JSON"))
        layout.addWidget(self.json_button)

        self.yaml_button = QPushButton("YAML", self)
        self.yaml_button.setStyleSheet("color: #EEEEEE; border: 2px solid #A91D3A; border-radius: 8px; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; font-family: sans-serif;")
        self.yaml_button.clicked.connect(lambda: self.select_output_format("YAML"))
        layout.addWidget(self.yaml_button)

        self.xml_button = QPushButton("XML", self)
        self.xml_button.setStyleSheet("color: #EEEEEE; border: 2px solid #A91D3A; border-radius: 8px; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; font-family: sans-serif;")
        self.xml_button.clicked.connect(lambda: self.select_output_format("XML"))
        layout.addWidget(self.xml_button)

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setStyleSheet("background-color: #C73659; color: #EEEEEE; border: none; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; margin-top: 16px; border-radius: 8px; font-family: sans-serif;")
        self.convert_button.clicked.connect(self.convert_files)
        
        layout.addWidget(self.convert_button)

    def select_input_file(self):
        file_dialog = QFileDialog()
        input_file, _ = file_dialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)")
        self.input_label.setText(f"Input File: {input_file}")
        self.input_file = input_file

    def select_output_format(self, output_format):
        print(f"Output format selected: {output_format}")
        self.output_format = output_format.lower()
        self.output_label.setText(f"Output Format: {output_format}")

    def convert_files(self):
        input_file = getattr(self, 'input_file', None)
        output_format = getattr(self, 'output_format', None)
        
        if not input_file or not output_format:
            print("Nie wybrano pliku wejściowego lub formatu wyjściowego.")
            return
        
        file_dialog = QFileDialog()
        file_filters = {
            "json": "JSON Files (*.json)",
            "yaml": "YAML Files (*.yaml)",
            "xml": "XML Files (*.xml)"
        }
        
        selected_filter = file_filters.get(output_format.lower())
        output_file, _ = file_dialog.getSaveFileName(self, "Select Output File", "", selected_filter)
        
        if not output_file:
            print("Nie wybrano pliku wyjściowego.")
            return

        self.load_file(input_file, output_format, output_file)

    def load_file(self, input_file, output_format, output_file):
        self.loader_thread = FileLoaderThread(input_file)
        self.loader_thread.data_loaded.connect(lambda data: self.save_file(data, output_format, output_file))
        self.loader_thread.error.connect(lambda error: print(f"Error loading file: {error}"))
        self.loader_thread.start()

    def save_file(self, data, output_format, output_file):
        self.saver_thread = FileSaverThread(data, output_file, output_format)
        self.saver_thread.success.connect(lambda message: print(message))
        self.saver_thread.error.connect(lambda error: print(f"Error saving file: {error}"))
        self.saver_thread.start()

def main():
    app = QApplication(sys.argv)
    converter_app = ConverterApp()
    converter_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
