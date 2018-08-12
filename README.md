# Autocomplete API

Web application writen with Flask which allows searching apps by their
 name using a REST API.

## Requirements

* flask
* datrie (implementation of a **Trie** data structure to
search by prefix)

Requirements can be installed via `requirements.txt` file:

```pip install -r requirements.txt```

## Configuration

Apps source file can be configured via configuration file
 `application.cfg` located at `instance` folder using
  `APPS_FILE`. Example:
  
  ```APPS_FILE='190titles.csv'```
  
## Run

Export to the terminal the application to work with
 by exporting the FLASK_APP environment variable and
 run flask:

```
export FLASK_APP=app.py
flask run
```

## Usage

The application exposes a REST api at `/` which allows
a `GET` request with an optional query param `prefix` to
 search name starting with specified prefix. If query
 param is not present, it will response with all app names.
 
Examples:

```/?prefix=fac```

## Testing

`tests` folder contains tests that can be run with *pytest*,
 i.e.:

````pytest tests/````