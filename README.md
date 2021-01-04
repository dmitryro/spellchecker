# SpellChecker API

### Running Service

To start service, run 

```bash
docker-compose up -d --scale worker=5 --no-recreate
```


### Running Tests

To run unit tests, first enter into container

```bash
 docker exec -it spellchecker_api bash
```

Then, run unit tests

```bash
 pytest pytest tests/test_endpoint.py
```


### Calling backend

To hit the endpoint, in a browser, Postman or any other app navigate to

```
http://0.0.0.0:31337/spell/CAR
```

You should be getting valid `200` response back

If, for example, you navigate to

```
http://0.0.0.0:31337/spell/crrr
```

You should be getting `400` and a list of suggestions.


### Using Swagger

To explore the API using swagger, navigate to


```
http://0.0.0.0:31337/apidocs
```



