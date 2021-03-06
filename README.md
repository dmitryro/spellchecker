# SpellChecker API

## Running Service

To build and start the service, run 
```bash
docker-compose up --build 
```

If you'd like to run in detached mode, run
```bash
docker-compose up -d 
```


## Running Tests

To run unit tests within, first enter the container

```bash
 docker exec -it spellchecker_api bash
```

Then, run unit tests

```bash
 pytest pytest tests/test_endpoint.py
```

All 8 tests should succeed.

### This covers the following test cases:

 ```test_get_route__failure__not_found``` 
  * This test is used to verify the word that was not found and not suggested like `asymptomaticcase`, returns 404.

 ```test_get_route__success__capitalized```
  * This test is used to verify the words like `Car` get properly recognized and processed.

 ```test_get_route__success__all_capital``` 
  * This test is used to verify the words like `CAR` and insure they get properly processed.

 ```test_get_route__success__repeated```
  * This test is used to identify and suggest words that have repeated non-vowels like `abandddon`.

 ```test_get_route__success__missing_vowel```
  * This test is used to identify and suggest words that have missing vowels like abndonmnt. 

 ```test_get_route__success__mixed```
  * This test is used to identify and suggest mixed cases of missing vowels, repeated non-vowels or mixed cases like `bllllLLlln`.

 ```test_base_route```
  * This test is used to verify the root location is accessible.

 ```test_get_route__success```
  * This test is used to verify and process words that exist as is in the dictionary, like `car`.

 ```test_get_route__success__invalid_case```
  * This test is used to verify and process words having invalid capitalization in their letters, like `caR`. Returns 200 and suggested correct spelling`.

### For the sake of this problem
  * We consider a word not to be found if it's neither located in dictionary nor suggested like `asymptomaticcase`.

## Calling backend

To hit the endpoint, in a browser, in Postman or using curl in termninal hit:

```
http://0.0.0.0:31337/spell/CAR
```

You should be getting valid `200` response back

If, for example, you navigate to

```
http://0.0.0.0:31337/spell/crrr
```

You should be getting `200` and a list of suggestions.

For a word that can't be neither found nor suggested, you'll get `400`, for example using

```
http://0.0.0.0.31337/spell/asymptomaticcase
```

## Using Swagger

To explore the API using swagger, navigate to


```
http://0.0.0.0:31337/apidocs
```


## Environment Variables used to set environment-specific values
* ```PROJECT_NAME```  - your project name to be used with ```docker-compose.yml```.
* ```DICT_PATH``` - the location of dictionary file.
* ```FLASK_HOST``` - The host used with the API.
* ```FLASK_PORT``` - The port used with the API.
* ```WORKERS``` - The number of ```gunicorn``` workers to run.
* ```TIMEOUT``` - The ```gunicorn``` timeout to be used.
* ```LOG_LEVEL``` - The default log level is set to ```DEBUG```. In production set ```INFO```.

The ```.env``` file contains the default values for environment variables used with the project.
