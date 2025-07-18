import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestGetFiles(unittest.TestCase):
    def testcalc(self):
        pass
        #print(f"{get_files_info("calculator", ".")}\n")
    
    def testpkg(self):
        pass
        #print(f"{get_files_info("calculator", "pkg")}\n")

    def testbin(self):
        pass
        #print(f"{get_files_info("calculator", "/bin")}\n")

    def testnondir(self):
        pass
        #print(f"{get_files_info("calculator", "../")}\n")

    def testlorem(self):
        print(run_python_file("calculator", "main.py"))
        print(run_python_file("calculator", "tests.py"))
        print(run_python_file("calculator", "../main.py"))
        print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    unittest.main()