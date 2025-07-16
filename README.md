# foolish_FastAPI
a simple API written using FastAPI, sqlalchemy, and pydantic

you'll need to create a venv

```bash
python -m venv venv
```

then activate that venv. This is operating system specific. On windows its  `venv\Scripts\activate.bat`

on linux it's `source venv/bin/activate`

then 
```bash
pip install fastapi[all] sqlalchemy
```

to launch the dev server you can run

```bash
fastapi dev main.py
```
to launch the server you can run 

```bash
fastapi run main.py
```
