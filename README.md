# tickie

Organise events fast and efficiently

# README

This generic `README.md` is a starting point. You might find further details in subfolder, e.g. for
the [backend](backend/README.md).

## Where to start?

The application can be run in Docker:
```bash
# build first:
docker-compose build

# run application:
docker-compose up

# destroy application:
docker-compose down -v
```

To verify all parts work, you can use those steps:

```shell
# Firstly, exec into the Docker container.
# To send an email to the given address, run:
./manage.py verify_mail recipient@example.com
# To create a user, run:
./manage.py createsuperuser
```

This user can login in /admin now and navigate to a user profile to upload a profile picture. This verifies that the
storage backend is also configured correctly (e.g. S3 bucket).

## ADRs

This project uses ADRs for all important decisions. Please read and update them in `/adrs/`.

## Hosting & Infrastructure

The infrastructure and its cost are described [here](infrastructure/HOSTING.md).

## Editorconfig

Please install a plugin for your IDE for [Editorconfig](https://editorconfig.org). This avoids different charsets, line
breaks etc. throughout the project.
