#!/usr/bin/env python
#
# @Author: Dalmasso Giovanni <gioda>
# @Date:   09-Feb-2018
# @Email:  giovanni.dalmasso@embl.es
# @Project: 3D reconstruction
# @Filename: colors.py
# @Last modified by:   gioda
# @Last modified time: 09-Feb-2018
# @License: MIT


"""Collection of basic colors as RGB for plotting (inspired by "Tableau" www.tableau.com)"""


def colBase10():
    """List of 10 basic colors as RGB."""
    col = [(31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40), (148, 103, 189),
           (140, 86, 75), (227, 119, 194), (127, 127, 127), (188, 189, 34), (23, 190, 207)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colLight():
    """List of 10 light colors as RGB."""
    col = [(174, 199, 232), (255, 187, 120), (152, 223, 138), (255, 152, 150), (197, 176, 213),
           (196, 156, 148), (247, 182, 210), (199, 199, 199), (219, 219, 141), (158, 218, 229)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colMedium():
    """List of 10 medium colors as RGB."""
    col = [(114, 158, 206), (255, 158, 74), (103, 191, 92), (237, 102, 93), (173, 139, 201),
           (168, 120, 110), (237, 151, 202), (162, 162, 162), (205, 204, 93), (109, 204, 218)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colCblind():
    """List of 10 color blind colors as RGB."""
    col = [(0, 107, 164), (255, 128, 14), (171, 171, 171), (89, 89, 89), (95, 158, 209),
           (200, 82, 0), (137, 137, 137), (162, 200, 236), (255, 188, 121), (207, 207, 207)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colGrey():
    """List of 5 grey colors as RGB."""
    col = [(207, 207, 207), (165, 172, 175), (143, 135, 130), (96, 99, 106), (65, 68, 81)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colTrafficLigth():
    """List of 9 traffic-light colors as RGB."""
    col = [(255, 193, 86), (219, 161, 58), (216, 37, 38), (177, 3, 24),
           (48, 147, 67), (255, 221, 113), (242, 108, 100), (159, 205, 153), (105, 183, 100)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colPurpleGrey():
    """List of 6 purple-grey colors as RGB."""
    col = [(220, 95, 189), (208, 152, 238), (153, 86, 136),
           (148, 145, 123), (123, 102, 210), (215, 213, 197)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col


def colBase20():
    """List of 20 basic colors as RGB."""
    col = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
           (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
           (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
           (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
           (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for j in range(len(col)):
        r, g, b = col[j]
        col[j] = (r / 255., g / 255., b / 255.)

    return col
