# DersEngine
#### Video Demo:  <https://vimeo.com/1010516735?share=copy>
#### Description:
DersEngine is a 2D image creation tool designed to help you create, edit, save, and manage tiles and pixel shapes for your projects. This tool provides an interactive command-line interface for generating and customizing tile images.

## Installation

Ensure you have the necessary dependencies installed:
- `Python 3.x`
- `Pillow` for image processing

You can install Pillow and random using pip:
pip install pillow
## Usage

Run the main script to start the DersEngine interactive command-line interface:

python main.py


## Main Menu
### create:
Create a new Tile Generator or Pixel Shape.
### edit:
Edit an existing Tile Generator or Pixel Shape.
### save:
Save a Tile Generator image to the specified directory.
### delete:
Delete a Tile Generator image or directory.
### list:
Display all existing Tile Generators and Pixel Shapes.
### end:
Exit the program.
## Create
- t: Create a Tile Generator.
- s: Create a Pixel Shape.
## Edit
- t: Edit a Tile Generator.
- s: Edit a Pixel Shape.
## Tile Generator Creation
You will be prompted to enter the following details:

- width: Width of the tile.
- height: Height of the tile.
- background color: Background color of the tile (e.g., 255, 255, 255 or 255, 255, 255, 255).
- line color: Line color of the tile (e.g., 0, 0, 0 or 0, 0, 0, 255).
- output file: Output file name with a valid extension (e.g., tile.png).
- output directory: Directory where the file will be saved.
## Pixel Shape Creation
You will be prompted to enter the following details:

- Tile Generator: Name of the Tile Generator to apply the shape to.
- coordinates: Coordinates of the shape (e.g., (1, 0), (1, 1), (1, 2)).
- color: Color of the shape (e.g., 255, 0, 0 or 255, 0, 0, 255).
### You can also specify repetition parameters:

- repeat: Whether the shape will be repeating (y or n).
- count_x: Number of horizontal repetitions.
- count_y: Number of vertical repetitions.
- spacing: Spacing between repetitions (e.g., 4, 4).
- starting: Starting coordinates for repetition (e.g., 0, 0).
- random cut: Option to randomly cut some pixels during repetition (y or n).
- cut chance: Chance for a pixel to be cut (between 0 and 1).
- cut color: Color to replace each cut pixel (e.g., 0, 0, 0 or 0, 0, 0, 0).
## Saving Tile Generators
You will be prompted to enter the following details:

- tile: Name of the tile to save.
- multiple copies: Whether to save multiple copies (y or n).
- count: Number of copies to save (if multiple copies is y).
## Deleting Tile Generators
- You will be prompted to enter the following details:

- file name: Name of the file to delete.
- delete directory: Option to delete the entire directory (y or n).
## Editing Tile Generators
You will be prompted to enter the following details:

- array: Width and height of the array.
- background color: Background color of the tile (e.g., 255, 255, 255 or 255, 255, 255, 255).
- line color: Line color of the tile (e.g., 0, 0, 0 or 0, 0, 0, 255).
- output file: Output file name with a valid extension (e.g., tile.png).
- output directory: Directory where the file will be saved.
## Editing Pixel Shapes
You will be prompted to enter the following details:

- coordinates: New coordinates of the shape (e.g., (1, 0), (1, 1), (1, 2)).
- color: New color of the shape (e.g., 255, 0, 0 or 255, 0, 0, 255).
- Classes
- TileGenerator
- Manages the creation and manipulation of tiles.

