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
