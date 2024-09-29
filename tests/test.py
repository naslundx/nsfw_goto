import unittest
import subprocess

from nsfw_goto import goto

class TestGotoMethod(unittest.TestCase):
    def _run_file(self, filename):
        process = subprocess.run(['python', filename], stdout=subprocess.PIPE, text=True)
        stdout = process.stdout.strip()
        return stdout

    def test_example_1(self):
        stdout = self._run_file('example1.py')
        result = int(stdout)

        self.assertEqual(result, 3)

    def test_example_2(self):
        stdout = self._run_file('example2.py')
        result = int(stdout)

        self.assertEqual(result, 300)

    def test_example_3(self):
        stdout = self._run_file('example3.py')

        self.assertEqual(stdout, 'hello world!\nhello world!\nend of outer if\n4')

    def test_example_4(self):
        stdout = self._run_file('example4.py')

        self.assertEqual(stdout, '1\n2')

    def test_example_5(self):
        stdout = self._run_file('example5.py')

        self.assertEqual(stdout, '1\n4')

    def test_example_6(self):
        stdout = self._run_file('example6.py')

        self.assertEqual(stdout, 'The secret is 123\nThe secret is 456')

if __name__ == '__main__':
    unittest.main()
