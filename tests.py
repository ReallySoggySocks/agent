import unittest
from functions.get_files_info import get_files_info

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

if __name__ == "__main__":
    unittest.main()