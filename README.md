Project structure:
                  * Base - the common methods that can be reused in the tests
                  * Pages - page object design pattern, here will be placed the reusable code divided by pages
                  * Tests - here will be placed all the tests
                  * venv folder - virtual environment (should be in the gitignore)

                         * gitignore file
                         * conftest.py - the code that will be used in every test
                         * pytest.ini - pytest configuration file
                         * requirements.txt - all the dependencies (libraries)


To run all the tests except of smoke: "pytest -m "not smoke",
smoke or sanity mark: "pytest -m "sanity or smoke",
smoke and sanity mark: "pytest -m "sanity and smoke",
to run all the tests: "pytest -v"




