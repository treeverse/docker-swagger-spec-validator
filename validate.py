#!/usr/bin/env python
import sys

from swagger_spec_validator import validate_spec_url
from swagger_spec_validator.common import SwaggerValidationError
from jsonschema import ValidationError


DEFAULT_SWAGGER_SPEC_LOCATION = '/mnt/swagger.json'


if __name__ == '__main__':
    spec = DEFAULT_SWAGGER_SPEC_LOCATION
    if len(sys.argv) > 1:
        spec = sys.argv[1]
    try:
        validate_spec_url(f'file://{spec}')
    except SwaggerValidationError as e:
        arg = e.args[1].args[1]
        while True:
            _, e = e.args
            if isinstance(e, ValidationError):
                print(e)
                sys.exit(1)
