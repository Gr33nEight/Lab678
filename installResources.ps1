# installResources.ps1
pip install PyQt5
pip install pyyaml
pip install pyinstaller

python -m PyInstaller --onefile --noconsole main.py


