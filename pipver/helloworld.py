"""! @brief Defines the the Hello World Class."""
##
# @file helloworld.py
#
# @brief Defines the hello world class.
#
# @section libraries_sensors Libraries/Modules
# - random standard library (https://docs.python.org/3/library/random.html)
#   - Access to randint function.
#
#
# @section author_sensors Author(s)
# - Created by Rafael Lyra on 31/01/2022.
#
# Copyright (c) 2022.  All rights reserved.

class HelloWorld:
    """! The Hello World base class.
    """

    def __init__(self):
        """!
        Initialize the text and call the main function
        """
        self.text = "Hello World!!"
        self.main()

    def main(self):
        """! Print Hello World """
        print(self.text)
