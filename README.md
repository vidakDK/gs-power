# GS Power

## Usage

1. Build Docker container and run it: `docker-compose up`
1. Access API endpoints:
```
0.0.0.0:8000/load
0.0.0.0:8000/generator
```

## Notes

- Used full Python Docker image instead of Alpine because building `numpy`, 
`scipy`, `matplotlib`, `numba`, `pandas` is time-consuming with Alpine, as we 
need to manually build all the C libraries.

## Future Improvements

1. Add Postgres database to store network parameters and information.
1. Add PUT/POST requests functionality to allow users to edit the network.
1. Integration tests with local HTTP server and local DB using `pytest-docker`.
1. More network parameters: 
    1. Power flow algorithm
    1. Trafo model
    1. Generator type
