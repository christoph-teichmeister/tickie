# tickie

Organise events fast and efficiently

## onrender.com

[web-service](https://dashboard.render.com/web/srv-cqqhr0jv2p9s73b81ktg)
[database](https://dashboard.render.com/d/dpg-cqqihpo8fa8c73fj116g-a)

[website](https://tickie-vvup.onrender.com)

## Where to start?

If you need a quickstart, please look at `pyproject.toml` first. It includes configuration of most tools. Secondly, you
should look into `Dockerfile` and `Pipfile`.

## Linting and formatting

This project Ruff for code formatting and linting, an extremely fast tool, to ensure consistent and clean code.

To format your code using **Ruff**, run:

```bash
ruff format .
```

To lint your code using **Ruff**, run:

```bash
ruff check .
```

or use it in watch mode

```bash
ruff check . --watch  # Automatically re-run on file changes
```

Furthermore we use DjHTML to lint our Django templates. To lint your templates using **DjHTML**, run:

```bash
djhtml .
```

## Environments and `.env`

There are multiple environment files to make the project usable in different scenarios:
- `development.env`:  This is the file with all settings to develop **locally** and is used with and without Docker.
- `unittest.env`:  This is the file with all settings to speed up tests. It's used for pytest.
- `docker-compose.env`:  This file is only used by Docker Compose for development with Docker.
- `.env`: There is no `.env` file because the defaults for all settings are defined in the settings-file and thy only
  need to be changed in the cases above (or in the Helm Chart for production usage). 

## Installing or updating packages with pipenv

The easiest option – as long as you do not have any special things going on – is to run `pipenv` locally:
```shell
pipenv update
```

If you need to run it in Docker, this can be done like that:
```shell
docker exec -it tickie-backend bash
pip install pipenv
    Installing collected packages: pipenv
      WARNING: The scripts pipenv and pipenv-resolver are installed in '/src/.local/bin' which is not on PATH.
      Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
/src/.local/bin/pipenv update
```
