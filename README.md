# GS Power

Minimal working example of a power network setup, power flow calculation, and
serving of the results through API endpoints. Power network setup and
calculation is done using [pandapower](http://github.com/e2nIEE/pandapower) and
API is implemented using the [Falcon](https://falconframework.org/) framework
and [gunicorn](https://gunicorn.org/) server. Python version used is `Python 3.7.5`.

Currently the network operates in RAM memory. When a `POST` request changes the
parameters they will stay that way until the Docker container is shut down, at
which point the changes will be lost. Naturally, this will be solved with a
database of any sort.

## Usage

1. Build Docker container and run it: `docker-compose up`
1. Access API endpoints:
```
http://0.0.0.0:8000/api/load
http://0.0.0.0:8000/api/generator
```

The endpoints allow `GET` and `POST` requests. `GET` accepts no parameters and
returns the result of the power flow, while `POST` allows editing of the 
Load and Generator elements, using a JSON body with the element specification. 

An example of a valid `body` for a `POST` request:
- Load endpoint: `{'p_mw': 0.5, 'q_mvar': 0.1}`
- Generator endpoint: `{'p_mw': 0.3}`


## Tests
To run tests locally:
```
pip install -r power_net/requirements.txt -r power_net/requirements-testing.txt
pytest power_net
```
## Notes

- Used full Python Docker image instead of Alpine because building `numpy`, 
`scipy`, `matplotlib`, `numba`, `pandas` is time-consuming with Alpine, as we 
need to manually build all the C libraries.

## TODOs

1. Add Postgres database to store network parameters and information.
1. Switch from `pip requirements` to `setuptools` and building a wheel.
1. More options for PUT/POST requests, to allow users to edit the network.
1. Integration tests with local HTTP server and local DB using `pytest-docker`.
1. More network parameters: 
    1. Power flow algorithm
    1. Trafo model
    1. Generator type
