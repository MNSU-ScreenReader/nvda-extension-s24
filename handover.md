# PyCharm Add-on for NVDA  

  

This add-on for PyCharm is designed to improve accessibility for users who are visually impaired and rely on the use of screen readers for everyday use and want to learn or improve their coding abilities.  

  

## Background  

  

The scope of this add-on is based off the previous work published by Dr. Guario Salivia and Dr. Flint Million involving Braille-based interaction with a specific assembly language IDE. The goal of this iteration of the project was to get indentation working with NVDA in the sense the user is read aloud the indentation level.  

  

## Features  

  

### NVDA Indentation Parser  

  

The NVDA screen reader addon incorporates a specialized parser that scans Python files to determine the overall indentation structure of the file. This parser identifies any inconsistencies in the indentation patterns within the file, providing insight into where to adjust the code.  

  

### Audible Indentation Feedback  

  

The addon is designed to audibly speak aloud the indentation level of the current line being navigated with the caret movement in a Python file. This feature aids developers using the screen reader in understanding the hierarchical structure of their code.  

  

### Function Detection and Output  

  

A feature of the addon is its ability to detect and output the function to which the current line belongs within a Python file. We did this by binding a gesture where if you press `NVDA + I` it will read aloud the function. This functionality assists developers in identifying the context and scope of their code, enabling more efficient and accurate code navigation.  

  

## Processes and Workflows 

**Indentation Parsing Process** 

  1. Define the Grammar or Rules 

     - Lexical Analysis 
       - Utilizing lexical analysis techniques to tokenize and parse Python code, specifically focusing on identifying indentation patterns.
         
     - Syntax Parsing 
       - Employing syntax parsing (e.g., using parsers like ast module in Python) to analyze the structure of Python code and extract indentation information.

     - Pattern Recognition
       -  Implementing algorithms to recognize and characterize indentation patterns within Python files, distinguishing between different levels of indentation and detecting inconsistencies, taking more of a string manipulation approach.
      
  2. Add-on parser integration
     - Utilizing NVDA's api, we detect the Python Text Editor where the code is located. Grabbing that information actively, we send it to me analyzed each time the user updates the caret position using the `event_caret` function where we also specifically grab the current line of text the caret is on.
  4. Function Detection
     - Parsing the Code:The ast.parse(code) function parses the given Python code string into an abstract syntax tree (tree)
     - Locating the Current Node: We traverse the AST (ast.walk(tree)) to find the node corresponding to the line_number where the caret is located within the code.
     - Finding the Enclosing Function: Traverse the AST (tree) and locate the nearest Function node that encapsulates the line corresponding to index 
 
## Resources
 - [NVDA Developer Guide](https://www.nvaccess.org/files/nvda/documentation/developerGuide.html)
 - [IntelliJ NVDA Addon](https://github.com/SamKacer/IntelliJ_NVDA_Addon.git)
 - [Eclipse NVDA Addon](https://github.com/albzan/eclipse-nvda.git)
 - [Notepad++ Addon](https://github.com/derekriemer/nvda-notepadPlusPlus.git)

## Next Steps
 1. Project List of Features to achieve
    - Debugging
    - Line by Line
    - Nesting
    - Back Track
    - Scope
    - Characters
    - Autocomplete
    - Relationship
 2. Project Research

  

  

  

  

  

 

 
