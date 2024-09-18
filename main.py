from classes.PixelShape import PixelShape
from classes.TileGenerator import TileGenerator

TILE_GENERATORS = {}
SHAPES = {}

def main():
    """
    Main function to handle user interaction for creating, editing, saving, and managing tiles and shapes.
    """

    while True:
        cmd = input("Welcome to the DersEngine, 2D image creation. Please enter a command (create, edit, save, delete, list or end):\n").strip().lower()
        if cmd == "end":
            break
        elif cmd == "create":
            while True:
                sub_cmd = input("Are we creating a Tilegenerator or shape? t/s?\n").lower()
                if sub_cmd == 's':
                    name = input("What will the name of this shape be?\n")
                    createPixelShape(name)
                    break
                elif sub_cmd == 't':
                    name = input("What will the name of the Tile Generator be?\n")
                    createTileGenerator(name)
                    break
                else:
                    print("Invalid Input, input s or t.")
        elif cmd == "edit":
            while True:
                sub_cmd = input("Are we editing a tile generator or shape? t/s or end to exit:\n".lower())
                if sub_cmd == 't':
                    editTile()
                elif sub_cmd == 's':
                    editShape()
                elif sub_cmd == 'end':
                    break
                else:
                    print("Invalid input please chose s for shape or t for tile generator, or end to go back.\n")
        elif cmd == "list":
            displayTiles()
            displayShapes()
        elif cmd == "save":
            saveTile()
        elif cmd == "delete":
            deleteTile()
        else:
            print(f"{cmd} is an invalid command please input a valid command.")

def createTileGenerator(name):
    """
    Creates a new TileGenerator object with user-defined parameters and stores it in the TILE_GENERATORS dictionary.

    Args:
        name (str): The name of the TileGenerator to create.
    """

    while True:
        width = input("What is the width?\n")
        height = input("What is the height?\n")
        back_c = input("Background color?: please type as x, x, x or x, x, x, x where x is an integer greater than 0 and less than 256:\n")
        line_c = input("Line color?: please type as x, x, x or x, x, x, x where x is an integer greater than 0 and less than 256:\n")
        output_file = input("Output file name? Please ensure it ends with .png, .jpg, .jpeg, .bmp, or .gif\n")
        output_directory = input("What will the directory the file is saved in be called?\n")

        try:
            height = int(height)
            width = int(width)
            back_c = tuple(map(int, back_c.split(',')))
            line_c = tuple(map(int, line_c.split(',')))
        except ValueError:
            print(f"{height} and {width} must be integers. {back_c} and {line_c} must be 3 or 4 integers.")
            continue
        TILE_GENERATORS[name] = TileGenerator(array = [["."]*width for _ in range(height)], background_color = back_c, line_color = line_c, output_file = output_file, output_directory = output_directory)
        break

def createPixelShape(name):
    """
    Creates a new PixelShape object and adds it to the SHAPES dictionary.

    Args:
        name (str): The name of the PixelShape to create.
    """

    while True:
        tile = input("What Tile Generator are we applying this shape too?\n" ).strip()
        if tile in TILE_GENERATORS:
            tile_generator = TILE_GENERATORS[tile]
        else:
            print("Tile Generator does not exist.")
            break
        coords = input("What are the coordinates of this shape? EX: (1, 0), (1, 1), (1, 2)\n")
        color = input("What color will this shape be? Enter as x, x, x or x, x, x, x where x is integer between 0 and 255:\n")
        try:
            coords = coords.strip('()').split('), (')
            coords = [tuple(map(int, coord.split(','))) for coord in coords]
            color = tuple(map(int, color.split(',')))
            if len(color) not in (3, 4):
                raise ValueError
        except ValueError:
            print("Invalid input for coordinates or color.")
            continue
        SHAPES[name] = PixelShape(tile_generator, coords, color = color)
        repeat = input("Will this shape be repeating? y/n?\n").lower()
        if repeat == 'y':
            try:
                count_x = int(input("How many times will we repeat the pattern horizontally?\n"))
                count_y = int(input("How many times will we repeat the pattern vertically?\n"))
                spacing = tuple(map(int, input("What will the spacing be horizantally and vertically? EX: 4, 4\n").split(',')))
                starting = tuple(map(int, input("Where would you like the repetition to start? EX: 0, 0 for beginning of Tile_Generator\n").split(',')))
                random = input("Would you like to randomly cut some pixels during repetition? y/n?\n").lower() == 'y'
                if random:
                    cut_chance = float(input("What chance would you like there to be for the pixel to cut, between 0 and 1. EX: 0.5\n"))
                    cut_color = tuple(map(int, input("What color would you like to replace each cut pixel with? EX: 0, 0, 0 or 0, 0, 0, 0?\n").split(',')))
                    SHAPES[name].repeat(count_x, count_y, spacing, starting, random, cut_chance, cut_color)
                    drawShape(name)
                    break
                else:
                    SHAPES[name].repeat(count_x, count_y, spacing, starting)
                    drawShape(name)
                    break
            except ValueError:
                print("Invalid input for repition parameters.\n")
                continue
        elif repeat == 'n':
            drawShape(name)
            break
        else:
            print("Please enter y or n for repeat.")
            continue

def drawShape(name):
    """
    Draws the shape identified by 'name' using its PixelShape instance.

    Args:
        name (str): The name of the shape to draw.
    """

    if name in SHAPES:
        SHAPES[name].draw()
    else:
        print("Shape does not exist.")

def saveTile():
    """
    Saves the tile specified by the user, either as a single image or multiple copies.
    """

    while True:
        tile = input("What tile will we be saving?\n")
        mult = input("Will there be more than one copy saved? y/n:\n").strip()
        if tile in TILE_GENERATORS and mult == 'y':
            count = int(input("How many copies?\n"))
            TILE_GENERATORS[tile].saveImage(multiples = True, count = count)
            print(f"{count} {tile}s have succesfully been saved to {TILE_GENERATORS[tile].output_directory}.")
            break
        elif tile in TILE_GENERATORS and mult == 'n':
            TILE_GENERATORS[tile].saveImage()
            print(f"{tile} succesfully saved to {TILE_GENERATORS[tile].output_directory}.")
            break
        else:
            print("Tile doesn't exist and/or improper input for mult")

def deleteTile():
    """
    deletes a specified tile from its file directory
    """

    while True:
        cmd = input("Please enter the name of the file you'd like to delete. end to exit.\n")
        if cmd.lower() == "end":
            print("Returning to menu.")
            break
        elif cmd in TILE_GENERATORS:
            while True:
                sub_cmd = input("Would you like to delete the directory as well? Warning doing so will delete all images within it.y/n\n").lower()
                if sub_cmd == 'y':
                    confirm = input(f"Are you positive you want to delete {TILE_GENERATORS[cmd].output_directory} y for yes any other key to cancel.\n").lower()
                    if confirm == 'y':
                        TILE_GENERATORS[cmd].deleteDirectory()
                        print("Directory succesfully deleted.")
                        break
                    else:
                        print("Going back.")
                        break
                elif sub_cmd == 'n':
                    try:
                        TILE_GENERATORS[cmd].deleteImage()
                        print(f"{cmd} succesfully deleted.")
                        break
                    except FileNotFoundError:
                        print(f"{cmd}'s file does not exist returning to tile selection.")
                        break
                else:
                    print(f"{sub_cmd} must be y or n.")
                    continue
        else:
            print(f"{cmd} not found")
            continue


def editTile():
    """
    Allows the user to edit the properties of an existing TileGenerator.
    """

    while True:
        tile = input("What tile generator will we be editing? end to quit:\n")
        if tile in TILE_GENERATORS:
            while True:
                cmd = input("What will we be editing? array(a), background color(bc), line color(lc), output file(of), output directory(od), or end to go back.\n")
                if cmd == 'a':
                    width = int(input("What width would you like?\n"))
                    height = int(input("What height would you like?\n"))
                    TILE_GENERATORS[tile].array = [["."]*width for _ in range(height)]
                elif cmd == 'bc':
                    color = input("What will the new color be? enter as x, x, x or x, x, x, x where x is an integer between 0 and 255:\n")
                    color = tuple(map(int, color.split(',')))
                    TILE_GENERATORS[tile].background_color = color
                elif cmd == 'lc':
                    color = input("What will the new color be? enter as x, x, x or x, x, x, x where x is an integer between 0 and 255:\n")
                    color = tuple(map(int, color.split(',')))
                    TILE_GENERATORS[tile].line_color = color
                elif cmd == 'of':
                    output_file = input("What will the new name be? don't forget to end with valid extension, i.e. .png, .jpg, .bmp, etc.\n")
                    TILE_GENERATORS[tile].output_file = output_file
                elif cmd == 'od':
                    output_directory = input("What will the new directory name be?\n")
                    TILE_GENERATORS[tile].output_directory = output_directory
                elif cmd == 'end':
                    print("Returning to generator selection.")
                    break
                else:
                    print("Invalid command use a, bc, lc, of, od, or end")
                    continue
        elif tile.lower() == 'end':
            print("Returning to shape/tile selection.")
            break

        else:
            print(f"{tile} not found.")

def editShape():
    """
    Allows the user to edit the properties of an existing PixelShape.
    """

    while True:
        shape = input("What shape will we be editing? end to quit\n")
        if shape in SHAPES:
            cmd = input("What will we be editing? Coords(cr) or color(co)? end to go back.\n")
            if cmd == "cr":
                coords = input("What will the new coordinates be? EX: (x, x), (x, x), (x, x)\n")
                try:
                    SHAPES[shape].tile_generator._applyBackground()
                    coords = coords.strip('()').split('), (')
                    coords = [tuple(map(int, coord.split(','))) for coord in coords]
                    SHAPES[shape].coords = coords
                    drawShape(shape)
                except (ValueError, IndexError):
                    print("Invalid Coords.")
            elif cmd == "co":
                color = input("What will the new color be? please enter in x, x, x or x, x, x, x format where x is between 0 and 255.\n")
                try:
                    SHAPES[shape].tile_generator._applyBackground()
                    color = tuple(map(int, color.split(',')))
                    SHAPES[shape].color = color
                    drawShape(shape)
                except ValueError:
                    print("Invalid Color")
            elif cmd.lower() == "end":
                print("Returning to shape selection.")
                break
        elif shape.lower() == "end":
            print("Returning to main menu.")
            break
        else:
            print(f"{shape} not found.")

def displayTiles():
    for key in TILE_GENERATORS.keys():
        print(f"{key}, ")

def displayShapes():
    for key in SHAPES.keys():
        print(f"{key}, ")


if __name__ == '__main__':
    main()

