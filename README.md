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
  * This test is used to verify the word that was not found and not suggested returns 404.

 ```test_get_route__success__capitalized```
  * This test is used to verify the words like `Car` get properly recognized and processed.

 ```test_get_route__success__all_capital``` 
  * This test is used to verify the words like `CAR` and insure they get properly processed.

 ```test_get_route__success__repeated```
  * This test is used to identify and suggest words that have repeated non-vowels like `abandddon`.

 ```test_get_route__success__missing_vowel```
  * This test is used to identify and suggest words that have missing vowels like abndonmnt. 

 ```test_get_route__failure__mixed```
  * This test is used to identify and suggest mixed cases of missing vowels, repeated non-vowels or mixed cases like `bllllLLlln`.

 ```test_base_route```
  * This test is used to verify the root location is accessible.

 ```test_get_route__success```
  * This test is used to verify and process words that exist as is in the dictionary, like `car`.

# For the sake of this problem we consider a word not to be found if it's neither located in dictionary nor suggested like `asymptomaticcase`.

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



