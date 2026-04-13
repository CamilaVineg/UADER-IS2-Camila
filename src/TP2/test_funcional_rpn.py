import unittest
import subprocess
import sys


class TestFuncionalRPN(unittest.TestCase):

    # -----------------------
    # CASOS FUNCIONALES BÁSICOS
    # -----------------------

    def test_suma_simple(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "3", "4", "+"],
            capture_output=True,
            text=True
        )

        self.assertIn("7", result.stdout)

    def test_expresion_compleja(self):
        result = subprocess.run(
            [sys.executable,
             "rpn.py",
             "5", "1", "2", "+", "4", "*", "+", "3", "-"],
            capture_output=True,
            text=True
        )

        self.assertIn("14", result.stdout)

    def test_raiz(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "9", "sqrt"],
            capture_output=True,
            text=True
        )

        self.assertIn("3", result.stdout)

    def test_trigonometria(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "90", "sin"],
            capture_output=True,
            text=True
        )

        self.assertTrue(
            "1" in result.stdout
        )

    # -----------------------
    # CASOS DE ERROR
    # -----------------------

    def test_division_por_cero(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "3", "0", "/"],
            capture_output=True,
            text=True
        )

        self.assertIn("Error", result.stdout)

    def test_token_invalido(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "3", "x", "+"],
            capture_output=True,
            text=True
        )

        self.assertIn("Error", result.stdout)

    def test_pila_incorrecta(self):
        result = subprocess.run(
            [sys.executable, "rpn.py", "3", "4"],
            capture_output=True,
            text=True
        )

        self.assertIn("Error", result.stdout)


if __name__ == "__main__":
    unittest.main()
