# Scholarship Flask REST API

This is an API created with the [Flask](https://flask.palletsprojects.com/en/1.1.x/) server that given a search query, returns a list of scholarships objects that matches that search term.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install Flask
pip install Flask-RESTful
```

## Usage

Use software such as Postman to test the outputs of the API

```python
class Scholarships(Resource):
    """This class takes in a query request argument q GET request and returns the result of the searchQuery function"""
    def get(self):
        args = request.args['q'].lower()
        return searchQuery(args)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)