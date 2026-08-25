# test_xeniris.py
"""
Tests for XenIris module.
"""

import unittest
from xeniris import XenIris

class TestXenIris(unittest.TestCase):
    """Test cases for XenIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XenIris()
        self.assertIsInstance(instance, XenIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XenIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
