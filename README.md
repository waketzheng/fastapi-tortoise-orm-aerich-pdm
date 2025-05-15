# fastapi-tortoise-orm-aerich-pdm
A mini demo for using pdm to manage deps of fastapi project that using tortoise-orm and aerich

## Steps

1. Install pdm
```bash
python -m pip install --upgrade pip pipx --user
pipx install pdm
```
2. Start project
```bash
pdm new fastapi_project
cd fastapi_project
pdm add fastapi uvicorn tortoise-orm asyncpg "aerich[toml]" loguru
pdm add --dev fast-dev-cli
source .venv/*/activate
```
3. Add src files
```bash
mkdir app
touch app/__init__.py
touch app/main.py
touch app/settings.py
touch app/models.py
#Edit files
# vi -O app/*.py
```
4. Initial db
```bash
aerich init -t app.settings.TORTOISE_ORM
aerich init-db
```
5. Runserver
```bash
export PYTHONPATH=.
pdm run python app/main.py
```
