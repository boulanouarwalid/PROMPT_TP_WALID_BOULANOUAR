import pytest
from product_formatter import format_product_code
from product_formatter_example import format_product_code as format_product_code_example
from product_formatter_multi_example import format_product_code as format_product_code_multi

# Tests for the first version (Zero-Shot)
class TestFormatProductCodeZeroShot:
    def test_valid_input(self):
        assert format_product_code("ABC1234DEF") == "ABC-1234-DEF"
        
    def test_invalid_length(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code("SHORT")
        assert "must be exactly 10 characters" in str(excinfo.value)
        
    def test_non_alphanumeric(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code("ABC123!DEF")
        assert "must contain only alphanumeric" in str(excinfo.value)
        
    def test_non_string_input(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code(12345)
        assert "must be a string" in str(excinfo.value)

# Tests for the second version (One-Shot)
class TestFormatProductCodeOneShot:
    def test_valid_input(self):
        assert format_product_code_example("ABC123DEF4") == "ABC-123-DEF4"
        
    def test_another_valid_input(self):
        assert format_product_code_example("XYZ987ABCD") == "XYZ-987-ABCD"
        
    def test_invalid_length(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code_example("SHORT")
        assert "must be exactly 10 characters" in str(excinfo.value)
        
    def test_non_alphanumeric(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code_example("ABC123!DEF")
        assert "must contain only alphanumeric" in str(excinfo.value)

# Tests for the third version (Few-Shot)
class TestFormatProductCodeFewShot:
    def test_valid_input(self):
        assert format_product_code_multi("ABC123DEF4") == "ABC-123-DEF4"
        
    def test_second_example_input(self):
        assert format_product_code_multi("XYZ987GHIJ") == "XYZ-987-GHIJ"
        
    def test_invalid_length(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code_multi("SHORT")
        assert "must be exactly 10 characters" in str(excinfo.value)
        
    def test_non_alphanumeric(self):
        with pytest.raises(ValueError) as excinfo:
            format_product_code_multi("ABC123!DEF")
        assert "must contain only alphanumeric" in str(excinfo.value)
        
    def test_edge_case_all_numbers(self):
        assert format_product_code_multi("1234567890") == "123-456-7890"
        
    def test_edge_case_all_letters(self):
        assert format_product_code_multi("ABCDEFGHIJ") == "ABC-DEF-GHIJ"