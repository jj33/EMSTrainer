# EMSTrainer Makefile — convenience targets

.PHONY: help validate exports

help:
    @echo "make validate   - run offline validator over examples/ and exports/"
    @echo "make exports    - render demo ACS exports (MD+CSV) to exports/demo/"

validate:
    @echo "Validating example/export files..."
    python3 tools/validate_examples.py

exports:
    @echo "Rendering demo ACS exports (MD+CSV) to exports/demo/..."
    python3 tools/export_smoke_test.py
