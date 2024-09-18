import os
import shutil
from classes import config
from PIL import Image, ImageDraw
class TileGenerator:
    """
    A class to generate and save tile images with specified attributes.

    Attributes:
        array (list of list): 2D array representing the tile.
        background_color (tuple): The background color of the tile, if none is specified background will be transparent.
        line_color (tuple): The color used for lines in the tile.
        output_file (str): The name of the output file.
        output_directory (str): The directory where the output file will be saved.
    """

    def __init__(self, array =  [["."]*32 for _ in range(32)], background_color = None, line_color = None, output_file = "temp_output.png", output_directory = "temp_assets"):
        """
        Initializes a new TileGenerator object.

        Args:
            array (list of list): 2D array representing the tile.
            background_color (tuple): The background color of the tile.
            line_color (tuple): The color used for lines in the tile.
            output_file (str): The name of the output file.
            output_directory (str): The directory where the output file will be saved.
        """

        self._array = array if isinstance(array, list) else  [["."]*32 for _ in range(32)]
        self._background_color = background_color if self.validateRGBA(background_color) else None
        self._line_color = line_color if self.validateRGBA(line_color) else None
        self._output_file = output_file if isinstance(output_file, str) and output_file.endswith(tuple(config.VALID_IMG_FILE_EXT.keys())) else "temp_output.png"
        self._output_directory = os.path.join(os.getcwd(), output_directory) if isinstance(output_directory, str) else "temp_assets"
        if not os.path.exists(self._output_directory):
            os.makedirs(self._output_directory)
        _, ext = os.path.splitext(self._output_file)
        mode = config.VALID_IMG_FILE_EXT.get(ext, "RGBA")
        self._img = Image.new(mode, (len(array[0]) if array else 0, len(array)), self._background_color)
        self._draw = ImageDraw.Draw(self._img)

        if self._background_color:
            self._applyBackground()

    def __str__(self):
        """
        Provides a string representation of the TileGenerator object.

        Returns:
            str: A description of the TileGenerator object.
        """

        return f"A Tile represented with a 2D array {self._array}, it has {self._background_color} as a background and {self._line_color} for lines. it will be saved as {self._output_file} in {self._output_directory}."

    @property
    def array(self):
        """
        Gets the current array of the Tilegenerator

        Returns:
            list of list: The current array of Tilegenerator.
        """

        return self._array

    @array.setter
    def array(self, array):
        """
        Sets a new array for the Tilegenerator

        Args:
            array(list of list): new 2D array to replace old array value.
        """

        self._array = array if isinstance(array, list) else [["."]*32]*32
        _, ext = os.path.splitext(self._output_file)
        mode = config.VALID_IMG_FILE_EXT.get(ext, "RGBA")
        self._img = Image.new(mode, (len(array[0]) if array else 0, len(array)), self._background_color)
        self._draw = ImageDraw.Draw(self._img)
        if self._background_color:
            self._applyBackground()

    @property
    def background_color(self):
        """
        Gets the current background color of the Tilegenerator

        Returns:
            tuple: The current background color of Tilegenerator.
        """

        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets a new background color for the Tilegenerator

        Args:
            background_color(tuple): tuple of either RGB or RGBA value to replace current one.
        """

        self._background_color = background_color if self.validateRGBA(background_color) else None
        self._applyBackground()

    @property
    def line_color(self):
        """
        Gets the current line color of the Tilegenerator

        Returns:
            tuple: The current line color of Tilegenerator.
        """

        return self._line_color

    @line_color.setter
    def line_color(self, line_color):
        """
        Sets a new line color for the Tilegenerator

        Args:
            line_color(tuple): tuple of either RGB or RGBA value to replace current one.
        """

        self._line_color = line_color if self.validateRGBA(line_color) else None

    @property
    def output_file(self):
        """
        Gets the current output file name of the Tilegenerator

        Returns:
            str: The current output file name of Tilegenerator.
        """

        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        """
        Sets a new output file name for the Tilegenerator

        Args:
            output_file(string): A string containing the new name for the output file, must end in valid extension located in config file.
        """

        if isinstance(output_file, str) and output_file.endswith(tuple(config.VALID_IMG_FILE_EXT.keys())):
            self._output_file = output_file
            _, ext = os.path.splitext(output_file)
            mode = config.VALID_IMG_FILE_EXT.get(ext, "RGBA")
            self._img = Image.new(mode, self._img.size, self._background_color)
            self._draw = ImageDraw.Draw(self._img)
            if self._background_color:
                self._applyBackground()
        else:
            self._output_file = "temp_file.png"
            _, ext = os.path.splitext(self._output_file)
            mode = config.VALID_IMG_FILE_EXT.get(ext, "RGBA")
            self._img = Image.new(mode, self._img.size, self._background_color)
            self._draw = ImageDraw.Draw(self._img)

    @property
    def output_directory(self):
        """
        Gets the current output directory of the Tilegenerator

        Returns:
            str: The current output directory of Tilegenerator.
        """

        return self._output_directory

    @output_directory.setter
    def output_directory(self, output_directory):
        """
        Sets a new output directory for the Tilegenerator, if one does not exist it will be made for you.

        Args:
            output_directory(string): the name of the new outpur directory.
        """

        self._output_directory = os.path.join(os.getcwd(), output_directory) if isinstance(output_directory, str) else "temp_assets"
        if not os.path.exists(self._output_directory):
            os.makedirs(self._output_directory)

    @staticmethod
    def validateRGBA(rgba):
        """
        A static method that verifies if a tuple fits the parameters for an RGB or RGBA color value.

        Args:
            rgba(tuple): the RGB or RGBA tuple value to check.

        Returns:
            bool: True if the value fits RGB or RGBA color code, False otherwise.
        """

        return isinstance(rgba, tuple) and (3 <= len(rgba) <= 4) and all(isinstance(c, int) and 0 <= c <= 255 for c in rgba)

    def _applyBackground(self):
        """
        A method used to apply the background color to the class object.
        """

        if self.background_color:
            for y, row in enumerate(self._array):
                for x, pixel in enumerate(row):
                    self._img.putpixel((x, y), self.background_color)

    def getSize(self):
        """
        A method to get the size of the Tilegenerator object.

        Returns:
            int: the highest of the two values between width and height.
        """

        return max(self._img.size)

    def saveImage(self, multiples = False, count = 1):
        """
        Saves the image with an optional of multiples saved and how many.

        Args:
            multiples(bool): a boolean expression True or False to determine if more than one copies being saved.
            count(int): how many copies of the image that will be saved.
        """

        if not isinstance(count, int) or count < 1 or not isinstance(multiples, bool):
            raise ValueError(f"{count} must be greater than or equal to 1 and {multiples} must be True or False")

        if multiples:
            for i in range(1, count + 1):
                self._img.save(os.path.join(self.output_directory, f"{i}_{self.output_file}"))
        else:
            self._img.save(os.path.join(self.output_directory, self.output_file))

    def deleteImage(self):
        """
        Deletes the file named in _output_file variable
        """

        os.remove(os.path.join(self.output_directory, self.output_file))

    def deleteDirectory(self):
        """
        Deletes the directory named in _output_directory and all it's contents
        """

        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)
        else:
            print(f"{self.output_directory} does not exist.")
