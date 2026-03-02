import pygame
from src.components.tiles import TestTile, SandTile
from settings import TILE_HEIGHT, TILE_WIDTH


def parse_level(file_path):
    """
    Parses level data from a file path given.

    Implemented by Jamie
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        for line in lines:
            new_line = []
            line = line.strip("\n")
            chars = list(line)

            for char in chars:
                match char:
                    case ".":
                        new_line.append("")
                    case "T":
                        new_line.append(SandTile)
            
            data.append(new_line)
        
    return data

def load_level(level_data, game):
    """
    Loads a level based off of the data given.

    Implemented by Jamie
    """
    for row_index, row in enumerate(level_data):
        for col_index, cell in enumerate(row):
            x = col_index * TILE_WIDTH
            y = row_index * TILE_HEIGHT

            print(cell, x, y)

            if cell == "":
                pass
            if cell == SandTile:
                new_tile = SandTile(x,y)
                game.render_layer.add(new_tile)
                game.tile_layer.add(new_tile)
