import pygame

import math
import numpy as np
import utils

# mainw_width, mainw_height = p.parameters["MAINW_WIDTH"], p.parameters["MAINW_HEIGHT"]
DEBUG = False
DEBUG_SWITCHED = False

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def draw_grid(grid, surface, alphasurf):
    global DEBUG_SWITCHED
    global DEBUG
    rdr = False
    for x in range(grid.width):
        for y in range(grid.height):
            t = grid.grid[x][y]

            # if (t.redraw or DEBUG) or DEBUG_SWITCHED:
            #     if DEBUG_SWITCHED and not DEBUG:
            #         DEBUG_SWITCHED = False
            if t.redraw:
                # if t.is_river or any([_t.is_river for _t in grid.get_neighbours_of(t, diag_neigh=True)]):
                #     rdr = True
                pygame.draw.rect(surface, t.get_color(), t.rect, 0)
                pygame.draw.rect(alphasurf, (0,0,0,0), t.rect, 0)
                # if t.tree != None:
                    # pygame.draw.circle(surface, 
                    #     (139,69,19,255),
                    #     # p.type2color["FOREST"],
                    #     t.middle, 
                    #     min(int(t.rect.w/2)-1, int(t.rect.h/2)-1),
                    #     0)
                for n in grid.get_neighbours_of(t, diag_neigh=True):
                    if not n.entities:
                        pygame.draw.rect(surface, n.get_color(), n.rect, 0)
                        pygame.draw.rect(alphasurf, (0,0,0,0), n.rect, 0)
                    # if n.is_forest:
                    #     # pygame.draw.rect(surface, p.type2color["FOREST"], n.rect, 0)
                    #     if n.tree != None:
                    #         pygame.draw.circle(surface, 
                    #             (139,69,19,255),
                    #             # p.type2color["FOREST"],
                    #             n.middle, 
                    #             min(int(n.rect.w/2)-1, int(n.rect.h/2)-1),
                    #             0)

                t.redraw = False

    # if rdr:
    # for rp in grid.rivers:
    #     pygame.draw.lines(surface, p.type2color["SHALLOW_WATER"], False, [t.middle for t in rp], 4)

def draw_healthbar(value, max_value, topleft, size, surface, c1=(255,0,0,255), c2=(0,255,0,255), min_value=0):
    factor = utils.normalise(value, min_value, max_value)

    pygame.draw.rect(surface, c1, pygame.Rect(topleft, size))
    if int(size[0]*factor) != 0:
        pygame.draw.rect(surface, c2, pygame.Rect(topleft, (int(size[0]*factor), size[1])))

def draw_path(start, path, grid, surface):
    points = [start.middle]
    for i in range(len(path)):
        _curr = path[i]
        _curr.redraw = True

        points.append(_curr.middle)

    pygame.draw.lines(surface, (64, 64, 64, 255), False, points, 1)

def draw_text(text, font, fontsize, surface, shift, x=10):
    displ_text = font.render(text, True, (0,0,0))
    surface.blit(displ_text, (x, fontsize*1.2 + shift))
    return shift + fontsize*1.2