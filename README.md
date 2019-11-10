# GS Power

## Usage

1) Build Docker container and run it:
```bash
docker-compose up
```

1) Access API endpoints:
```bash
0.0.0.0:8000/load
0.0.0.0:8000/generator
```

## Notes

- Used full Python Docker image instead of Alpine because building `numpy`, 
`scipy`, `matplotlib`, `numba`, `pandas` is difficult with Alpine, as we need
to manually include all the C libraries.