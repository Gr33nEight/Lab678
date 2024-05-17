# Projekt Konwertera Danych

## Opis

Projekt Konwertera Danych jest aplikacją umożliwiającą konwersję danych między formatami **'.xml'**, **'.json'** i **'.yaml'** (.yml). Program pozwala użytkownikowi na łatwe wczytywanie danych z jednego formatu, a następnie zapisanie ich w innym formacie, zachowując poprawność składniową.

## Funkcje
- Wczytywanie danych z plików **'.xml'**, **'.json'** i **'.yaml'** (.yml).
- Konwersja danych z jednego formatu na drugi.
- Zapisywanie przekonwertowanych danych w wybranym formacie.
  
## Instalacja
1. Upewnij się, że masz zainstalowanego Pythona w wersji 3.x.
2. Sklonuj lub pobierz repozytorium z kodem aplikacji.
3. Przejdź do katalogu projektu.
4. Zalecane jest utworzenie i aktywowanie wirtualnego środowiska Pythona:

bash
Skopiuj kod
```
python -m venv venv
source venv/bin/activate  # Dla systemów Unix/Linux
.\venv\Scripts\activate    # Dla systemu Windows
```
5. Zainstaluj wymagane biblioteki za pomocą polecenia:
```
bash
Skopiuj kod
pip install -r requirements.txt
```

## Użycie

Aby uruchomić program, wykonaj następujące kroki:

1. Uruchom skrypt installResources.ps1, aby zainstalować potrzebne komponenty Pythona:
```
bash
Skopiuj kod
.\installResources.ps1
```
2. Wywołaj program, podając jako argumenty ścieżki do plików wejściowych i wyjściowych:
```
bash
Skopiuj kod
program.exe pathFile1.x pathFile2.y
```
Zadania do wykonania
Projekt składa się z następujących zadań:

- **Task0:** Utworzenie skryptu installResources.ps1 do instalacji potrzebnych komponentów Pythona.
- **Task1:** Parsowanie argumentów przekazywanych przy uruchomieniu programu.
- **Task2:** Wczytywanie danych z pliku .json i weryfikacja poprawności składni.
- **Task3:** Zapis danych do pliku .json zgodnie ze składnią.
- **Task4:** Wczytywanie danych z pliku .yml i weryfikacja poprawności składni.
- **Task5:** Zapis danych do pliku .yml zgodnie ze składnią.
- **Task6:** Wczytywanie danych z pliku .xml i weryfikacja poprawności składni.
- **Task7:** Zapis danych do pliku .xml zgodnie ze składnią.
- **Task8:** Utworzenie wersji programu z interfejsem użytkownika (UI).
- **Task9:** Wersja UI umożliwiająca asynchroniczne wczytywanie i zapisywanie danych.

## Automatyzacja budowania

Projekt został skonfigurowany do automatycznego budowania przy użyciu GitHub Actions. Workflow został ustawiony tak, aby budować plik .exe i przesyłać go do repozytorium GitHub po każdym pushu do gałęzi master.

## Uwagi

- Projekt został stworzony z myślą o przewidywalności i zabezpieczeniu przed błędnym działaniem oraz nieprawidłowymi danymi wejściowymi.
- Python posiada gotowe biblioteki do obsługi formatów .json, .xml i .yaml, jednak wymagają one dodatkowej instalacji przez pip.

## Autor
Projekt został stworzony przez: Natanael Jop (Gr33nEight).
 
 
