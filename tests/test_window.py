"""
Unit tests for the Window class.

Tests the core Window functionality including initialization,
UI building, and window properties.
"""

import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
from tkinter_open_url.tk.window import Window


class TestWindow:
    """Test suite for the Window class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Reason: Avoid actual GUI creation during tests
        self.mock_tk_patcher = patch('tkinter.Tk.__init__')
        self.mock_tk_init = self.mock_tk_patcher.start()
        self.mock_tk_init.return_value = None

    def teardown_method(self):
        """Clean up after each test method."""
        self.mock_tk_patcher.stop()

    def test_window_initialization_default_params(self):
        """
        Test Window initialization with default parameters.
        
        Expected use case: Creating a window with default title and geometry.
        """
        # Arrange & Act
        with patch.object(Window, 'title') as mock_title, \
             patch.object(Window, 'geometry') as mock_geometry, \
             patch.object(Window, 'lift') as mock_lift, \
             patch.object(Window, 'attributes') as mock_attributes, \
             patch.object(Window, 'after_idle') as mock_after_idle:
            
            window = Window()
            
            # Assert
            mock_title.assert_called_once_with("Window Title")
            mock_geometry.assert_called_once_with("500x500")
            mock_lift.assert_called_once()
            mock_attributes.assert_called_with("-topmost", True)
            mock_after_idle.assert_called_once()

    def test_window_initialization_custom_params(self):
        """
        Test Window initialization with custom parameters.
        
        Expected use case: Creating a window with custom title and geometry.
        """
        # Arrange
        custom_title = "Custom Test Window"
        custom_geometry = "800x600"
        
        # Act
        with patch.object(Window, 'title') as mock_title, \
             patch.object(Window, 'geometry') as mock_geometry, \
             patch.object(Window, 'lift') as mock_lift, \
             patch.object(Window, 'attributes') as mock_attributes, \
             patch.object(Window, 'after_idle') as mock_after_idle:
            
            window = Window(title=custom_title, geometry=custom_geometry)
            
            # Assert
            mock_title.assert_called_once_with(custom_title)
            mock_geometry.assert_called_once_with(custom_geometry)
            mock_lift.assert_called_once()

    def test_window_initialization_empty_title(self):
        """
        Test Window initialization with empty title.
        
        Edge case: Empty string as title parameter.
        """
        # Arrange & Act
        with patch.object(Window, 'title') as mock_title, \
             patch.object(Window, 'geometry') as mock_geometry, \
             patch.object(Window, 'lift') as mock_lift, \
             patch.object(Window, 'attributes') as mock_attributes, \
             patch.object(Window, 'after_idle') as mock_after_idle:
            
            window = Window(title="")
            
            # Assert
            mock_title.assert_called_once_with("")
            mock_geometry.assert_called_once_with("500x500")

    def test_window_initialization_invalid_geometry(self):
        """
        Test Window initialization with invalid geometry string.
        
        Failure case: Invalid geometry format should not crash initialization.
        """
        # Arrange & Act
        with patch.object(Window, 'title') as mock_title, \
             patch.object(Window, 'geometry') as mock_geometry, \
             patch.object(Window, 'lift') as mock_lift, \
             patch.object(Window, 'attributes') as mock_attributes, \
             patch.object(Window, 'after_idle') as mock_after_idle:
            
            # Should not raise exception during initialization
            window = Window(geometry="invalid_geometry")
            
            # Assert
            mock_geometry.assert_called_once_with("invalid_geometry")
            # Reason: tkinter.geometry() will handle invalid format internally

    def test_build_method_calls_all_sections(self):
        """
        Test that build() method calls all section building methods.
        
        Expected use case: Building complete UI with all sections.
        """
        # Arrange
        with patch.object(Window, '__init__', return_value=None), \
             patch.object(Window, 'build_default_section') as mock_default, \
             patch.object(Window, 'build_language_section') as mock_language, \
             patch.object(Window, 'build_code_section') as mock_code, \
             patch.object(Window, 'build_financial_section') as mock_financial, \
             patch.object(Window, 'build_youtube_section') as mock_youtube:
            
            window = Window()
            
            # Act
            window.build()
            
            # Assert
            mock_default.assert_called_once()
            mock_language.assert_called_once()
            mock_code.assert_called_once()
            mock_financial.assert_called_once()
            mock_youtube.assert_called_once()

    def test_window_inherits_from_tk(self):
        """
        Test that Window class properly inherits from tk.Tk.
        
        Expected use case: Verify inheritance structure.
        """
        # Act & Assert
        assert issubclass(Window, tk.Tk)

    def test_window_has_required_methods(self):
        """
        Test that Window class has all required methods.
        
        Expected use case: Verify method existence.
        """
        # Arrange
        required_methods = [
            'build',
            'build_default_section',
            'build_language_section', 
            'build_code_section',
            'build_financial_section',
            'build_youtube_section'
        ]
        
        # Act & Assert
        for method_name in required_methods:
            assert hasattr(Window, method_name), f"Window missing method: {method_name}"
            assert callable(getattr(Window, method_name)), f"Window.{method_name} is not callable"
