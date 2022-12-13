# Python Testing (More specificially Unittest) Notes

#### Red-Green-Refactor:
* Test-driven development is a software  development process which relies on requirements being converted to test cases before the code is written
* Red - Write a test that fails - no code written yet
* Green - The test is passed - code is written in order to pass
* Refactor - Update code so it is more efficient and passes the test

#### Terms:
* A test case is a single test which test a particular thing. 
* A test suite is a grouping of test cases into a set of tests that belong together.
* A test fixture is used to ensure that there is a well-known and fixed environment in which tests are run so that results are repeatable. E.g. Loading a DB with a known set of data

#### Unittest Library:
* Unittest requires that our test  filename starts with the word `test` followed by an underscore and a descriptive name of what we’re testing.
* If we don’t start the method name with the word test, it will be ignored and won't run, when we run the test file.
* See sample unittests in test_evens.py and test_student.py files

#### Lifecycle of a Test:
* `setUp` runs at the start of each test method, so can keep code DRY by creating a function in camelCase at start to create a relevant instance.
* The `tearDown` method can be used to remove temporary files, folders or close a connection to a database and is runa fter every test.
* Can't use `setUp` to run code to prepopulate a database etc. as it runs at the start of each test, but there is `setUpClass` case that can be used. Similarly, a `tearDownClass`.
* Runs are in the form of:<br/>
`setUpClass`<br/>
{for each test}`setUp`-> `Test`-> `tearDown`<br/>
`tearDownClass`
