from .i18n import I18N

i18n = I18N(path='locale')

import lib.tester as tester
import lib.functions as functions

def test_variable_defined_correct_value():
    namespace = {"answer": 42}
    expected_message = "Great job! Variable 'answer' is correctly defined with the right value of 42."
    assert tester.variable_definition(namespace) == expected_message

def test_variable_defined_incorrect_value():
    namespace = {"answer": 43}
    expected_message = "Variable 'answer' is incorrectly defined. Expected value was 42, but got 43."
    assert tester.variable_definition(namespace) == expected_message

def test_variable_not_defined():
    namespace = {}
    expected_message = "Variable 'answer' is not defined. Please define it."
    assert tester.variable_definition(namespace) == expected_message

def test_variable_defined_correct_value_custom_name():
    namespace = {"result": 42}
    expected_message = "Great job! Variable 'result' is correctly defined with the right value of 42."
    assert tester.variable_definition(namespace, variable_name="result") == expected_message

def test_variable_defined_incorrect_value_custom_name():
    namespace = {"result": 43}
    expected_message = "Variable 'result' is incorrectly defined. Expected value was 42, but got 43."
    assert tester.variable_definition(namespace, variable_name="result") == expected_message

def test_variable_not_defined_custom_name():
    namespace = {}
    expected_message = "Variable 'result' is not defined. Please define it."
    assert tester.variable_definition(namespace, variable_name="result") == expected_message

def test_arithmetic_operations_correct_value():
    namespace = {"result": 34}
    expected_message = "Great job! Variable 'result' is correctly defined with the right value of 34.0."
    assert tester.arithmetic_operations(namespace) == expected_message

def test_arithmetic_operations_incorrect_value():
    namespace = {"result": 30}
    expected_message = "Variable 'result' is incorrectly defined. Expected value was 34.0, but got 30."
    assert tester.arithmetic_operations(namespace) == expected_message

def test_arithmetic_operations_not_defined():
    namespace = {}
    expected_message = "Variable 'result' is not defined. Please define it."
    assert tester.arithmetic_operations(namespace) == expected_message

def test_blackbody_radiation_correct():
    def student_func(wavelength, temp):
        # Correct implementation of blackbody radiation function
        return functions.blackbody_radiation(wavelength, temp)
    
    expected_message = "All tests passed! Your implementation appears to be correct."
    assert tester.blackbody_radiation(student_func) == expected_message

def test_blackbody_radiation_incorrect():
    def student_func(wavelength, temp):
        # Incorrect implementation of blackbody radiation function
        return 0
    
    expected_message = "\n".join([
        "Scenario Visible light, approx. sun's surface temp failed:",
        "Wavelength=5e-07 m and temperature=5778 K.",
        "Expected result was close to 2.64e+13 W/m^2/sr/m, but got 0.00e+00.",
        "",
        "Scenario Microwave, approx. CMB temp failed:",
        "Wavelength=0.001 m and temperature=2.725 K.",
        "Expected result was close to 6.10e-04 W/m^2/sr/m, but got 0.00e+00.",
    ])
    assert tester.blackbody_radiation(student_func) == expected_message

def test_blackbody_radiation_not_implemented():
    def student_func(wavelength, temp):
        # Not implemented function
        return None
    
    expected_message = "Blackbody Radiation function not implemented. Skipping tests."
    assert tester.blackbody_radiation(student_func) == expected_message

def test_peak_wavelength_correct():
    def student_func(temp):
        # Correct implementation of Wien's Law function
        return functions.peak_wavelength(temp)
    
    expected_message = "All tests passed! Your implementation appears to be correct."
    assert tester.peak_wavelength(student_func) == expected_message

def test_peak_wavelength_incorrect():
    def student_func(temp):
        # Incorrect implementation of Wien's Law function
        return 0
    
    expected_message = "\n".join([
        "Scenario Sun's surface temperature failed:",
        "Temperature=5778 K.",
        "Expected peak wavelength was close to 5.01e-07 m, but got 0.00e+00 m.",
        "",
        "Scenario Sirius Star temperature failed:",
        "Temperature=9940 K.",
        "Expected peak wavelength was close to 2.91e-07 m, but got 0.00e+00 m.",
        "",
        "Scenario Cool red star failed:",
        "Temperature=3000 K.",
        "Expected peak wavelength was close to 9.66e-07 m, but got 0.00e+00 m.",
        "",
        "Scenario Incandescent light bulb failed:",
        "Temperature=2400 K.",
        "Expected peak wavelength was close to 1.21e-06 m, but got 0.00e+00 m.",
        "",
        "Scenario Hot blue star failed:",
        "Temperature=20000 K.",
        "Expected peak wavelength was close to 1.45e-07 m, but got 0.00e+00 m.",
    ])
    assert tester.peak_wavelength(student_func) == expected_message

def test_peak_wavelength_not_implemented():
    def student_func(temp):
        # Not implemented function
        return None
    
    expected_message = "Wien's Law function not implemented. Skipping tests."
    assert tester.peak_wavelength(student_func) == expected_message



