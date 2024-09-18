import random
from .TileGenerator import TileGenerator
class PixelShape:
    """
    A class to define and draw pixel shapes on a TileGenerator.

    Attributes:
        tile_generator (TileGenerator): The TileGenerator instance to draw the shape on.
        coords (list of tuples): Coordinates of the shape.
        color (tuple): The color of the shape.
        rounded_edges(bool): not currently utilized, but one determine if the shape is rounded in the future.
    """

    def __init__(self, tile_generator, coords, color, rounded_edges = False):
        """
        Initializes a new PixelShape object.

        Args:
            tile_generator (TileGenerator): The TileGenerator object to draw the shape on.
            coords (list of tuples): Coordinates of the shape.
            color (tuple): The color of the shape.
            rounded_edges(bool): not currently utilized, but one determine if the shape is rounded in the future.
        """

        self._tile_generator = tile_generator if isinstance(tile_generator, TileGenerator) else None
        self._coords = coords if isinstance(coords, list) else []
        self._color = color if TileGenerator.validateRGBA(color) else None
        self._rounded_edges = rounded_edges if isinstance(rounded_edges, bool) else False

    def __str__(self):
        """
        Provides a string representation of the Pixelshape object.

        Returns:
            str: A description of the Pixelshape object.
        """

        return f"A custom pixel shape on {self._tile_generator} at {self._coords} coordinates in {self._color} color. Rounded edges is {self._rounded_edges}"

    @property
    def tile_generator(self):
        """
        Gets the current TileGenerator of the PixelShape object.

        Returns:
            TileGenerator: The current TileGenerator of PixelShape object.
        """

        return self._tile_generator

    @tile_generator.setter
    def tile_generator(self, tile_generator):
        """
        Sets a new TileGenerator object for the PixelShape object.

        Args:
            tile_generator(TileGenerator): new TileGenerator object to replace old TileGenerator object of PixelShape.
        """

        if isinstance(tile_generator, TileGenerator):
            self._tile_generator = tile_generator
        else:
            print("Must use a valid TileGenerator object.\n")

    @property
    def coords(self):
        """
        Gets the current coords of the PixelShape object.

        Returns:
            list of tuples: The current coords of PixelShape object.
        """

        return self._coords

    @coords.setter
    def coords(self, coords):
        """
        Sets new coords for the PixelShape object.

        Args:
            coords(list of tuples): new coords to replace the old coords of PixelShape object.
        """

        self._coords = coords if isinstance(coords, list) else []

    @property
    def color(self):
        """
        Gets the current color of the PixelShape object.

        Returns:
            tuple: The current color of PixelShape object.
        """

        return self._color

    @color.setter
    def color(self, color):
        """
        Sets a new color for the PixelShape object.

        Args:
            color(tuple): new color to replace the old color of the PixelShape object.
        """

        self._color = color if self._tile_generator.validateRGBA(color) else None

    @property
    def rounded_edges(self):
        """
        Gets whether the PixelShape object has rounded edges.

        Returns:
            bool: rounded edges of PixelShape object.
        """

        return self._rounded_edges

    @rounded_edges.setter
    def rounded_edges(self, rounded_edges):
        """
        Sets whether the PixelShape object has rounded edges.

        Args:
            rounded_edges(bool): Whether the PixelShape object has rounded edges True or False.
        """

        self._rounded_edges = rounded_edges if isinstance(rounded_edges, bool) else False

    def draw(self, radius = 2):
        """
        Draws the shape onto the TileGenerator, if rounded edges is flagged radius will be used.

        Args:
            radius(int): the radius of the ellipse if rounded edges is flagged.
        """

        for coord in self.coords:
            x, y = coord
            if self.rounded_edges:
                self.tile_generator._draw.ellipse([x - radius, y - radius , x + radius, y + radius], fill = self.color)
            else:
                self.tile_generator._img.putpixel((x, y), self.color)

    def repeat(self, count_x = 5, count_y = 5, spacing = (4, 4), start_pixel = (0, 0), randomize = False, cut_chance = 0.5, cut_color = None):
        """
        Repeats the pattern defined by the coordinates across the tile image, with options for spacing, randomization, and cutting.

    Args:
        count_x (int): Number of times to repeat the pattern horizontally. Defaults to 5.
        count_y (int): Number of times to repeat the pattern vertically. Defaults to 5.
        spacing (tuple of int): The spacing between repeated patterns in the x and y directions. Defaults to (4, 4).
        start_pixel (tuple of int): The starting coordinates for the repetition. Defaults to (0, 0).
        randomize (bool): If True, applies a random cut to some pixels based on the cut_chance. Defaults to False.
        cut_chance (float): The probability of cutting a pixel when randomize is True. Should be between 0 and 1. Defaults to 0.5.
        cut_color (tuple): The color to use for pixels that are cut (randomized). If None, uses the background color. Defaults to None.
        """

        new_coords = []
        img_width, img_height = self.tile_generator._img.size
        start_x, start_y = start_pixel
        for i in range(count_x):
            for j in range(count_y):
                for coord in self.coords:
                    new_x = coord[0] + i * spacing[0]
                    new_y = coord[1] + j * spacing[1]
                    if new_x < img_width and new_y < img_height:
                        if randomize and (new_x - start_x) % spacing [0] == 0 and (new_y - start_y) % spacing[1] == 0:
                            if random.random() > cut_chance:
                                self.tile_generator._img.putpixel((new_x, new_y), cut_color)
                            else:
                                self.tile_generator._img.putpixel((new_x, new_y), self.color)
                        else:
                            new_coords.append((new_x, new_y))
        self.coords = new_coords

