import sys
import json

def parse_arguments():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

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