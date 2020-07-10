# python-flask-angular-1-backend

ready to deploy to heroku

## Heroku

Open repository then

```
git push heroku master
```

to update the API running [here](https://enigmatic-oasis-17388.herokuapp.com/)

## Server logs

To see server log use

```
export HEROKU_APP=enigmatic-oasis-17388
heroku logs -n 100
```

## API documentation

Endpoints:

* ``/exams``: for example ``curl https://enigmatic-oasis-17388.herokuapp.com/exams``
* ``/time``: for example ``curl https://enigmatic-oasis-17388.herokuapp.com/time``

## Database

Rather than just having ``app.db`` as a local file, we can connect to a postgres server running on Heroku as well.

To create the postgres DB run:

```
export HEROKU_APP=enigmatic-oasis-17388
heroku addons:create heroku-postgresql:hobby-dev
```

at this point we could migrate an existing database using ``pg:copy``.
