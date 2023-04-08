import unittest

from base16_colorlib.color import __version__ as color_version
from base16_colorlib.color_scheme import __version__ as color_scheme_version
from base16_colorlib import (
    Color,
    aquarium,
    ashes,
    ayu_dark,
    ayu_light,
    bearded_arc,
    blossom_light,
    catppuccin_latte,
    catppuccin_frappe,
    catppuccin_macchiato,
    catppuccin_mocha,
    dracula,
    decay,
    everblush,
    everforest_dark,
    everforest_light,
    falcon,
    gruvbox_dark,
    gruvbox_light,
    kanagawa,
    melange,
    monokai,
    monochrome,
    mountain,
    nord,
    onedark,
    onelight,
    rosepine,
    rosepine_moon,
    rosepine_dawn,
    rxyhn,
    solarized,
    sweetpastel,
    tokyodark,
    tokyonight,
    yoru,
)

color_schemes = [
    aquarium,
    ashes,
    ayu_dark,
    ayu_light,
    bearded_arc,
    blossom_light,
    catppuccin_latte,
    catppuccin_frappe,
    catppuccin_macchiato,
    catppuccin_mocha,
    dracula,
    decay,
    everblush,
    everforest_dark,
    everforest_light,
    falcon,
    gruvbox_dark,
    gruvbox_light,
    kanagawa,
    melange,
    monokai,
    monochrome,
    mountain,
    nord,
    onedark,
    onelight,
    rosepine,
    rosepine_moon,
    rosepine_dawn,
    rxyhn,
    solarized,
    sweetpastel,
    tokyodark,
    tokyonight,
    yoru,
]


class TestBase16ColorLibVersion(unittest.TestCase):
    def test_base16_colorlib_version(self):
        self.assertEqual(color_version, '0.1.0')
        self.assertEqual(color_scheme_version, '0.1.0')


class TestСlassColorExternalColorScheme(unittest.TestCase):
    test_cls_color = Color()
    test_hex_colors = {
        "scheme": "onedark",
        "author": "https://github.com/one-dark",
        "base00": "#1e222a",
        "base01": "#353b45",
        "base02": "#3e4451",
        "base03": "#545862",
        "base04": "#565c64",
        "base05": "#abb2bf",
        "base06": "#b6bdca",
        "base07": "#c8ccd4",
        "base08": "#e06c75",
        "base09": "#d19a66",
        "base0A": "#e5c07b",
        "base0B": "#98c379",
        "base0C": "#56b6c2",
        "base0D": "#61afef",
        "base0E": "#c678dd",
        "base0F": "#be5046",
    }
    test_rgb_colors = {
        "scheme": "onedark",
        "author": "https://github.com/one-dark",
        "base00": (30, 34, 42),
        "base01": (53, 59, 69),
        "base02": (62, 68, 81),
        "base03": (84, 88, 98),
        "base04": (86, 92, 100),
        "base05": (171, 178, 191),
        "base06": (182, 189, 202),
        "base07": (200, 204, 212),
        "base08": (224, 108, 117),
        "base09": (209, 154, 102),
        "base0A": (229, 192, 123),
        "base0B": (152, 195, 121),
        "base0C": (86, 182, 194),
        "base0D": (97, 175, 239),
        "base0E": (198, 120, 221),
        "base0F": (190, 80, 70),
    }

    @staticmethod
    def _remove_meta_fields(**color_scheme):
        color_scheme.pop('scheme')
        color_scheme.pop('author')
        return color_scheme

    def test_hex_to_rgb_and_rgb_to_hex_returns_correct_type(self):
        test_hex_colors = self._remove_meta_fields(**self.test_hex_colors)
        for key, value in test_hex_colors.items():
            rgb_color = self.test_cls_color.hex_to_rgb(value)
            hex_color = self.test_cls_color.rgb_to_hex(*rgb_color)
            self.assertIsInstance(rgb_color, tuple)
            self.assertIsInstance(hex_color, str)

    def test_hex_to_rgb_and_rgb_to_hex_correct_value(self):
        test_hex_colors = self._remove_meta_fields(**self.test_hex_colors)
        for key, value in test_hex_colors.items():
            benchmark_hex = value
            benchmark_rgb = self.test_rgb_colors[key]
            rgb_color = self.test_cls_color.hex_to_rgb(benchmark_hex)
            hex_color = self.test_cls_color.rgb_to_hex(*benchmark_rgb)
            self.assertEqual(hex_color, benchmark_hex)
            self.assertEqual(rgb_color, benchmark_rgb)


class TestСlassColorInternalColorSchemes(unittest.TestCase):
    color_schemes = color_schemes
    test_cls_color = Color()

    @staticmethod
    def _remove_meta_fields(**color_scheme):
        color_scheme.pop('scheme')
        color_scheme.pop('author')
        return color_scheme

    def test_hex_to_rgb_and_rgb_to_hex_returns_correct_type(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                rgb_color = self.test_cls_color.hex_to_rgb(value)
                hex_color = self.test_cls_color.rgb_to_hex(*rgb_color)
                self.assertIsInstance(hex_color, str)
                self.assertIsInstance(rgb_color, tuple)

    def test_hex_to_rgb_and_rgb_to_hex_correct_value(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                benchmark_hex = value
                rgb_color = self.test_cls_color.hex_to_rgb(benchmark_hex)
                hex_color = self.test_cls_color.rgb_to_hex(*rgb_color)
                self.assertEqual(hex_color, benchmark_hex)


if __name__ == "__main__":
    unittest.main()
