"""
Tests for the scanner module.
"""

import pytest
from w2_scanner.scanner import W2Scanner


class TestW2Scanner:
    """Test cases for W2Scanner class."""

    def test_scanner_initialization(self):
        """Test that scanner can be initialized."""
        scanner = W2Scanner()
        assert scanner is not None

    def test_scan_method_exists(self):
        """Test that scan method exists."""
        scanner = W2Scanner()
        assert hasattr(scanner, 'scan')
        assert callable(scanner.scan)


if __name__ == "__main__":
    pytest.main([__file__])

