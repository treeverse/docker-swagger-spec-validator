# docker-swagger-spec-validator

This is a simple Docker image that wraps [sawgger_spec_validator](https://github.com/Yelp/swagger_spec_validator).
It provides a `validate.py` script that accepts a swagger json file path which is then passed to the `validate_spec_url` validation function provided by sawgger_spec_validator.

Used by [lakeFS](https://github.com/treeverse/lakeFS) to validate its swagger spec against the swagger 2.0 specification.

## Example Usage

```sh
swagger expand --format=json swagger.yml > /tmp/swagger.json
docker run --rm -it -v /tmp/swagger.json:/mnt/swagger.json treeverse/sawgger_spec_validator:latest
```
