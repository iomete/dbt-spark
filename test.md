
## Run sample dbt

```shell

source .toxrunner/bin/activate

# install globally
pip3 install .

cd sample-test/test1
jdbc:hive2://dwh-910848238944.iomete.com/;transportMode=http;ssl=true;httpPath=reporting/cliservice
```

## Run integration test

```shell
tox -e integration-iomete

tox -e integration-spark-thrift
tox -e integration-spark-databricks-http
```

## Run unit tests
```shell
TOXENV: "unit"
PYTEST_ADDOPTS: "-v --color=yes --csv unit_results.csv"

tox

----

tox -e unit
```