# python-text-editor
Text Editor in python Tkinter as beginner project. 
This document outlines the structure and functionalities of a text editor created using tkinter in Python.

## Overview

The text editor allows users to perform basic operations such as opening, saving, and editing text files. It provides a user-friendly interface for text manipulation and editing.

## Project Components

### Window Creation

The GUI window is created using tkinter. It includes various frames for organizing different sections of the editor:

- Vertical Button Frame (`frame_btns`)
- Horizontal Button Frame (`horizontal_frame`)
- Text Box Frame (`frame_txt`)
- Status Bar (`status_bar`)

### Main Functionalities

- **New File**: Clears the text box for creating a new file.
- **Open File**: Allows users to select and open a text file.
- **Save File**: Saves the current content to an existing file.
- **Save As File**: Prompts users to save the content in a new file.
- **Clear Text**: Clears the text box content.
- **Exit**: Closes the text editor.

### Edit Functionalities

- **Bold Text**: Makes the selected text bold or removes bold formatting.
- **Italic Text**: Makes the selected text italic or removes italic formatting.
- **Undo**: Reverts the most recent text edit.
- **Redo**: Reapplies the undone edit.

### GUI Layout

- Vertical Buttons: Open, New, Save, Save As, Clear, Exit.
- Horizontal Buttons: Bold (B), Italic (I), Redo (R), Undo (U).

### Code Components

The code utilizes functions to handle various operations and button commands, including file operations, text editing, and GUI configurations. 

- Functions for file operations (`open_file`, `save_file`, `save_as_file`, `new_file`, `clear_file`).
- Functions for text editing (`make_bold`, `make_italic`, `undo`, `redo`).

