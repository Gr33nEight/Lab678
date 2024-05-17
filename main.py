import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
import yaml
import json
import xml.etree.ElementTree as xml
from functools import partial

def load_json(input_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Nie można wczytać pliku JSON: {e}")
        sys.exit(1)

def save_json(data, output_file):
    try:
        if isinstance(data, xml.Element):
            data_dict = _xml_to_dict(data)
            with open(output_file, 'w') as file:
                json.dump(data_dict, file, indent=4)
        else:
            with open(output_file, 'w') as file:
                json.dump(data, file, indent=4)
        print(f"Dane zostały zapisane do pliku {output_file}")
    except Exception as e:
        print(f"Nie można zapisać danych do pliku JSON: {e}")
        sys.exit(1)

def load_yaml(input_file):
    try:
        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except Exception as e:
        print(f"Nie można wczytać pliku YAML: {e}")
        sys.exit(1)

def save_yaml(data, output_file):
    try:
        with open(output_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print(f"Dane zostały zapisane do pliku {output_file}")
    except Exception as e:
        print(f"Nie można zapisać danych do pliku YAML: {e}")
        sys.exit(1)

def load_xml(input_file):
    try:
        tree = xml.parse(input_file)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Nie można wczytać pliku XML: {e}")
        sys.exit(1)

def save_xml(data, output_file):
    try:
        with open(output_file, 'w') as file:
            xml_string = xml.tostring(data).decode()
            file.write(xml_string)
        print(f"Dane zostały zapisane do pliku {output_file}")
    except Exception as e:
        print(f"Nie można zapisać danych do pliku XML: {e}")
        sys.exit(1)

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
    result = {}
    for child in element:
        if child is not None:
            child_dict = _xml_to_dict(child)
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child_dict)
                else:
                    result[child.tag] = [result[child.tag], child_dict]
            else:
                result[child.tag] = child_dict
        else:
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child.text)
                else:
                    result[child.tag] = [result[child.tag], child.text]
            else:
                result[child.tag] = child.text
    return result

def convert_logic(output_format, input_file, output_file):
    if input_file.endswith('.json'):
        if output_format.lower() == 'json':
            data = load_json(input_file)
            save_json(data, output_file)
        elif output_format.lower() == 'yaml':
            data = load_json(input_file)
            save_yaml(data, output_file)
        elif output_format.lower() == 'xml':
            data = load_json(input_file)
            root = xml.Element("data")
            _convert_to_xml_recursive(data, root)
            save_xml(root, output_file)
        else:
            print("Nieobsługiwany format pliku wyjściowego.")
            sys.exit(1)
    elif input_file.endswith('.yaml'):
        if output_format.lower() == 'json':
            data = load_yaml(input_file)
            save_json(data, output_file)
        elif output_format.lower() == 'yaml':
            data = load_yaml(input_file)
            save_yaml(data, output_file)
        elif output_format.lower() == 'xml':
            data = load_yaml(input_file)
            root = xml.Element("data")
            _convert_to_xml_recursive(data, root)
            save_xml(root, output_file)
        else:
            print("Nieobsługiwany format pliku wyjściowego.")
            sys.exit(1)
    elif input_file.endswith('.xml'):
        if output_format.lower() == 'json':
            data = load_xml(input_file)
            save_json(data, output_file)
        elif output_format.lower() == 'yaml':
            data = load_xml(input_file)
            save_yaml(data, output_file)
        elif output_format.lower() == 'xml':
            data = load_xml(input_file)
            save_xml(data, output_file)
        else:
            print("Nieobsługiwany format pliku wyjściowego.")
            sys.exit(1)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.init_ui()
    def init_ui(self):
        layout = QVBoxLayout()

        self.input_label = QLabel("Input File:")
        layout.addWidget(self.input_label)

        self.input_button = QPushButton("Select Input File")
        self.input_button.clicked.connect(self.select_input_file)
        layout.addWidget(self.input_button)

        self.output_label = QLabel("Output File:")
        layout.addWidget(self.output_label)

        self.json_button = QPushButton("JSON")
        self.json_button.clicked.connect(partial(self.select_output_format, "JSON"))
        layout.addWidget(self.json_button)

        self.yaml_button = QPushButton("YAML")
        self.yaml_button.clicked.connect(partial(self.select_output_format, "YAML"))
        layout.addWidget(self.yaml_button)

        self.xml_button = QPushButton("XML")
        self.xml_button.clicked.connect(partial(self.select_output_format, "XML"))
        layout.addWidget(self.xml_button)

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_files)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

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
        
        filename_parts = output_file.split('.')
        if len(filename_parts) > 1:
            output_file = '.'.join(filename_parts[:-1])

        if not output_file.endswith(tuple(selected_filter.split()[-2:])):
            output_file += f".{output_format.lower()}"
        
        print(f"Output_format { output_format }, input_file { input_file }, output_file { output_file }")
        convert_logic(output_format, input_file, output_file)
        print(f"Konwertowanie {input_file} do {output_file}")

def main():
    app = QApplication(sys.argv)
    converter_app = ConverterApp()
    converter_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()