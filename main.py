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