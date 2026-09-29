"""
1. Terminal Setting :
Setting--> Tool--> Terminal--> Shell Path --> "C:\\WINDOWS\\system32\\cmd.exe"

2. Install Imp Libraries :
    below are the command(terminal):
    1. pip install pytest
    2. pip install selenium
    3. pip install webdriverManager
    4. pip install pytest-xdist
    5. pip install pytest-html
    6. pip install pytest-rerunfailures
    7. pip install openpyxl
    8. pip install faker
    9. pip install pytest-sugar
    10. pip install pytest-cov --> your task

3. Set default test runner :
Setting--> Tool--> Python Integrated Tool --> Testing --> Default test runner --> Select "Pytest"

4. Rules For pytest:
    1. For Pytest we have to create the class under the class
       we have to create the methods and that methods are nothing but the test cases.
    2. Class name should start with  "Test".
    3. Method/Testcase name should start with "test_".
    4. File name should start with "test_" or ends with "_test".
    5. Method name should be unique.

5. Test Run Commands(Terminal):
    1. If you want to run all the test cases in folder then :
        command --> pytest
    2. Standard output and verbose output just For more information about test case execution and output
        command --> pytest -s -v
    3. If you want to run the test cases in specific file then:
        command --> pytest "testCases/test_case_file_name.py"
        e.g. --> "pytest -s -v "testCases/test_file1.py"
        e.g. --> "pytest -s -v "testCases/test_file2.py"
    4. If you want to run the specific test case :
        command1 --> pytest -k "testcase_name"
        command2 --> pytest testCases/test_file2.py::Test002::test_mul_006 -v -s
    5.  To disable warnings :
        pytest --disable-warnings
    6. To run test case parallel : (pytest-xdist)
        command1 --> pytest -n auto
        command2 --> pytest -n=2
        (-n=num, num--> no. of worker processor)
    7. Grouping the testcases :
        command1 --> pytest -m "group_name"
        command2 --> pytest -m "group_name1 and group_name2"
        command3 --> pytest -m "group_name1 or group_name2"
        command4 --> pytest -m not "group_name1"

        e.g. --> pytest -m "sanity"
        e.g. --> pytest -m "sanity and regression"
        e.g. --> pytest -m "sanity or regression"
        e.g. --> pytest -m "not sanity"

    8. To create HTML reports for testcase execution: (pytest-html)
    command : pytest --html=folder_name/report_name.html
    e.g. : pytest --html=HTMLReports/my_report.html -n auto

    9. To rerun failed testcases :
    command : pytest -v -s --reruns= number_of_reruns --reruns-delay= Time_in secs
    e.g. : pytest -v -s --reruns=2 --reruns-delay=1
    add decorator : @pytest.mark.flaky(reruns=2, reruns_delay=1)

"""
import pytest


class Test001:

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_sum_001(self, demo_fixture):
        a = 10
        b = 20
        print(f"Sum of {a} + {b} = {a + b}")
        assert a + b == 30

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_002(self,demo_fixture):
        assert True


    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.sanity
    #@pytest.mark.xfail
    def test_003(self, demo_fixture):
        assert False

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.sanity
    @pytest.mark.regression
   #@pytest.mark.skip
    def test_mul_004(self, demo_fixture):
        a = 10
        b = 20
        print(f"Mul of {a} * {b} = {a * b}")
        assert a * b == 200


    def mul_005(self): # This method is not starting with 'test_' Pytest will not consider this as a test case and exclude from the execution .
        a = 2
        b = 5
        print(f"Mul of {a} * {b} = {a * b}")
        assert a * b == 10