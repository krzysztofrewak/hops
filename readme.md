## hops
This repository will contain all hop data gathered from Hopsteiner website and other services. Data will be used in academic projects.

## Installation
The project requires Python 3.9+. To install dependencies, run:

```bash
pip install -r requirements.txt
```

## Features
### Stats
Project includes a simple tool for generating statistics about included hop varieties. Run:

```bash
python3 -m utils.stats
```

### JSON Validator
Project includes a simple tool for validating JSON5 hop variety files using a JSON Schema definition. All hop data files in `./data/` should follow a consistent structure defined in `hops.json`. To validate all JSON5 files inside `./data/`, run:

```bash
python3 -m utils.validate
```
