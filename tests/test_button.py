"""
Unit tests for the Button class.

Tests the core Button functionality including initialization,
configuration, and grid placement.
"""

import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock, call
from tkinter_open_url.tk.button import Button


class TestButton:
    """Test suite for the Button class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Reason: Create a mock frame for button placement during tests
        self.mock_frame = MagicMock()
        
        # Reason: Mock tkinter Button to avoid GUI creation during tests
        self.mock_button_patcher = patch('tkinter.Button.__init__')
        self.mock_button_init = self.mock_button_patcher.start()
        self.mock_button_init.return_value = None

    def teardown_method(self):
        """Clean up after each test method."""
        self.mock_button_patcher.stop()

    def test_button_initialization_default_params(self):
        """
        Test Button initialization with default parameters.
        
        Expected use case: Creating a button with minimal configuration.
        """
        # Arrange & Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid:
            
            button = Button(self.mock_frame)
            
            # Assert
            self.mock_button_init.assert_called_once_with(
                self.mock_frame, 
                text=None, 
                command=None, 
                relief=None, 
                bd=None
            )
            # Reason: Default text should be configured when text is None
            mock_config.assert_any_call(text="None_00")
            # Reason: Default command should print message when command is None
            mock_config.assert_any_call(command=mock_config.call_args_list[1][1]['command'])
            mock_grid.assert_called_once_with(row=0, column=0)

    def test_button_initialization_custom_params(self):
        """
        Test Button initialization with custom parameters.
        
        Expected use case: Creating a button with specific configuration.
        """
        # Arrange
        custom_text = "Click Me"
        custom_command = lambda: print("Custom command")
        custom_relief = tk.FLAT
        custom_bd = 5
        custom_row = 2
        custom_column = 3
        
        # Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid:
            
            button = Button(
                self.mock_frame,
                row=custom_row,
                column=custom_column,
                text=custom_text,
                command=custom_command,
                relief=custom_relief,
                bd=custom_bd
            )
            
            # Assert
            self.mock_button_init.assert_called_once_with(
                self.mock_frame,
                text=custom_text,
                command=custom_command,
                relief=custom_relief,
                bd=custom_bd
            )
            # Reason: No config calls should be made when all params are provided
            mock_config.assert_not_called()
            mock_grid.assert_called_once_with(row=custom_row, column=custom_column)

    def test_button_initialization_none_text_generates_default(self):
        """
        Test Button initialization with None text generates position-based text.
        
        Edge case: None text should generate text based on row/column position.
        """
        # Arrange
        row, column = 1, 2
        
        # Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid:
            
            button = Button(self.mock_frame, row=row, column=column, text=None)
            
            # Assert
            expected_text = f"None_{row}{column}"
            mock_config.assert_any_call(text=expected_text)

    def test_button_initialization_none_command_sets_default(self):
        """
        Test Button initialization with None command sets default print command.
        
        Edge case: None command should set a default lambda that prints a message.
        """
        # Arrange & Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid, \
             patch('builtins.print') as mock_print:
            
            button = Button(self.mock_frame, command=None)
            
            # Assert
            # Reason: Verify that config was called with a command
            assert mock_config.call_count >= 1
            command_call = None
            for call_args in mock_config.call_args_list:
                if 'command' in call_args[1]:
                    command_call = call_args[1]['command']
                    break
            
            assert command_call is not None, "Default command should be set"
            
            # Act: Execute the default command
            command_call()
            
            # Assert: Default command should print the expected message
            mock_print.assert_called_once_with("Command is not configured")

    def test_button_inherits_from_tk_button(self):
        """
        Test that Button class properly inherits from tk.Button.
        
        Expected use case: Verify inheritance structure.
        """
        # Act & Assert
        assert issubclass(Button, tk.Button)

    def test_button_grid_placement_with_different_positions(self):
        """
        Test Button grid placement with various row/column combinations.
        
        Expected use case: Verify correct grid positioning.
        """
        # Arrange
        test_positions = [(0, 0), (1, 2), (5, 10), (0, 3)]
        
        for row, column in test_positions:
            with patch.object(Button, 'config') as mock_config, \
                 patch.object(Button, 'grid') as mock_grid:
                
                # Act
                button = Button(self.mock_frame, row=row, column=column)
                
                # Assert
                mock_grid.assert_called_once_with(row=row, column=column)

    def test_button_initialization_with_empty_string_text(self):
        """
        Test Button initialization with empty string text.
        
        Failure case: Empty string text should not trigger default text generation.
        """
        # Arrange & Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid:
            
            button = Button(self.mock_frame, text="")
            
            # Assert
            self.mock_button_init.assert_called_once_with(
                self.mock_frame,
                text="",
                command=None,
                relief=None,
                bd=None
            )
            # Reason: Empty string is not None, so no default text should be set
            # Only command should be configured since it's None
            mock_config.assert_called_once()
            call_args = mock_config.call_args_list[0]
            assert 'command' in call_args[1]
            assert 'text' not in call_args[1]

    def test_button_initialization_preserves_frame_reference(self):
        """
        Test that Button initialization preserves the frame reference.
        
        Expected use case: Button should be associated with the correct parent frame.
        """
        # Arrange
        specific_frame = MagicMock()
        
        # Act
        with patch.object(Button, 'config') as mock_config, \
             patch.object(Button, 'grid') as mock_grid:
            
            button = Button(specific_frame)
            
            # Assert
            # Reason: First argument to tk.Button.__init__ should be the frame
            self.mock_button_init.assert_called_once()
            call_args = self.mock_button_init.call_args
            assert call_args[0][0] is specific_frame
