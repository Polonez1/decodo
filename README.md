# Decodo Google Scraper

CLI aplikacja w Pythonie do uruchamiania scrapera Google Search z użyciem Decodo Scraper API.

## Instalacja Pythona

Projekt wymaga Pythona w wersji 3.9 lub nowszej.

Pobierz Pythona z:
https://www.python.org/downloads/

Podczas instalacji na Windows zaznacz:
Add Python to PATH

## Sprawdzenie wersji Pythona

Po instalacji otwórz terminal i sprawdź wersję:

```bash
python --version
```

## GIT instaliavimas

GIT instaliuojame iš:
https://git-scm.com/install/

po instaliavimo patikriname versija

```bash
git --version
```

## Terminalo atidarymas

Atidarome terminala folderyje, kur gulės projektas.

![Terminal](readme_data/Terminal.png)

## Klonuojame GIT repozitoriją

```bash
git clone https://github.com/your-username/decodo.git
```

## Instaliuojame bibliotekas

```bash
pip install -r requirements.txt
```

## Autentifikacija

Sukuriame failą login.py ir įklijuojame:

```bash
token = "YOUR_BASE64_TOKEN"
```

## Paleidžiame apps'ą

Terminale įrašome komandą:
```bash
python run.py --search_by homeopatija --page_from 1 --page_count 10
```

