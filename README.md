# Dokumentacja projektu DevOps (Flask + Docker)

## Jak uruchomić projekt

### Wymagania:
1. Zainstalowany Docker.
2. Dostęp do GitHub Codespaces (lub zainstalowane środowisko obsługujące Git oraz Python).

---

### Instrukcje uruchomienia:

1. **Sklonuj repozytorium projektu z GitHub:**
    ```bash
    git clone https://github.com/LasekM/DevOps_Project.git
    ```

2. **Zbuduj obraz Dockera:**
    ```bash
    docker build -t flask_app:1.0.0 .
    ```

3. **Uruchom kontener:**
    ```bash
    docker run -d -p 8080:8080 flask_app:1.0.0
    ```

4. **Sprawdź aplikację w przeglądarce:**
    - Otwórz przeglądarkę internetową.
    - Wpisz adres: `http://localhost:8080`
    - W środowisku Codespaces użyj linku dostarczonego przez platformę (zwykle coś w stylu `https://your-space-name-8080.preview.app.github.dev/`).

### Dodatkowe informacje:
- **Dockerfile**: Plik konfiguracyjny Dockera zawierający szczegóły budowy aplikacji.
- **Struktura aplikacji:**
  - `app.py`: Główny plik aplikacji Flask.
  - `templates/index.html`: Szablon aplikacji.
  - `static/css/style.css`: Wygląd aplikacji.

Po zakończeniu testowania zatrzymaj kontener:
```bash
docker stop [CONTAINER_ID]
```

Gotowe!

