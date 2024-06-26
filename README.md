﻿# Projekt Konwertera Danych

## Opis

Projekt Konwertera Danych jest aplikacją umożliwiającą konwersję danych między formatami **.xml**, **.json** i **.yaml** (.yml). Program pozwala użytkownikowi na łatwe wczytywanie danych z jednego formatu, a następnie zapisanie ich w innym formacie, zachowując poprawność składniową.

## Funkcje

- Wczytywanie danych z plików **.xml**, **.json** i **.yaml** (.yml).
- Konwersja danych z jednego formatu na drugi.
- Zapisywanie przekonwertowanych danych w wybranym formacie.
  
## Instalacja

1. Przejdź do zakładki **Actions**
2. Kliknij w najnowszy **Workflow run**
3. Przescrolluj do zakładki **Artifacts**
4. Pobierz plik **exe-artifact** 

## Automatyzacja budowania

Projekt został skonfigurowany do automatycznego budowania przy użyciu GitHub Actions. Workflow został ustawiony tak, aby budować plik .exe i przesyłać go do repozytorium GitHub po każdym pushu do gałęzi main.

## Uwagi

- Projekt został stworzony z myślą o przewidywalności i zabezpieczeniu przed błędnym działaniem oraz nieprawidłowymi danymi wejściowymi.

## Informacje

Program ten jest częścią projektu na zaliczenie przedmiotu Narzędzia pracy w branży IT. Poniżej wypisane są poszczególne zadania, które należało wykonać

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

#### Dodatkowo aby skorzystać z wersji konsolowej należy skolować projekt z branchu **Finished-Basic-Converter**


## Autor
Projekt został stworzony przez: Natanael Jop (Gr33nEight).

