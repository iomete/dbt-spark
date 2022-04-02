def pytest_configure(config):
    config.addinivalue_line(
        "markers", "profile_apache_spark"
    )
