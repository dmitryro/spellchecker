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

# This covers the following test cases:

 ```test_get_route__failure__not_found``` 
  * This test is used to verify the word that was not found and not suggested returns 404

 ```test_get_route__success__capitalized```
  * This test is used to verify the words like `Car` get properly recognized and processed

 


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



