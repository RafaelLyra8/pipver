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
    """!
    The Hello World base class.

    Information
    ===========

     Attributes
    ----------

    text : str ::

        A string that is outputed as the hello world

    Methods
    -------
    main()
        Prints the animals name and what sound it makes

    >>> print 'This is a doctest block'
        This is a doctest block
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

class City:
    """!
        The base class of a city.

        Attributes
        ----------
        - says_str : str
            - a formatted string to print out what the animal says
        - name : str
            - the name of the animal
        - sound : str
            - the sound that the animal makes
        - num_legs : int
            - the number of legs the animal has (default 4)

        Methods
        -------
        says(sound=None)
            Prints the animals name and what sound it makes
    """

    def __init__(self):
        """!
        Initialize the variables
        """
        self.mayorList = [
            "Rosting", "Denk"]
        self.name = "Sclatky"
        self.coordinates = (0.34, 23.43)
        self.area = 125.32
        self.population = 1523623

    def getArea(self) -> float:
        """!
        Get the city area.
        """
        return self.area

    def getCoordinates(self) -> tuple(float):
        """!
        Get the city coordinates.
        """
        return self.coordinates

    def getName(self) -> str:
        """!
        Get the city name.
        """
        return self.name

    def setName(self, name: str) -> str:
        """!
        Set the city name.
        """
        self.name = name

    def setMayors(self, mayorList: list(str)) -> list(str):
        """!
        @param x: This is a description of
            the parameter x to a function.
            Note that the description is
            indented four spaces.
        @type x: This is a description of
            x's type.
        @return: This is a description of
            the function's return value.

        It contains two paragraphs.
        """
        self.mayorList = mayorList
