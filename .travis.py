language: python
python:
  - "3.4.4"
install:
  - "pip install ."
script:
  - "python setup.py test"
