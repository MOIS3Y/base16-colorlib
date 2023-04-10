import unittest

from base16_colorlib.version import __version__ as package_version
from base16_colorlib.utils import __version__ as color_version
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
        self.assertEqual(package_version, '0.2.0')
        self.assertEqual(color_version, '0.2.0')
        self.assertEqual(color_scheme_version, '0.2.0')


class TestСlassColorExternalColorScheme(unittest.TestCase):

    def setUp(self):
        self.test_cls_color = Color()
        self.test_hex_colors = {
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
        self.test_rgb_colors = {
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
        self.test_hsl_colors = {
            "scheme": "onedark",
            "author": "https://github.com/one-dark",
            "base00": (0.6111111111111112, 0.16666666666666666, 0.1411764705882353),  # noqa: E501
            "base01": (0.6041666666666666, 0.1311475409836065, 0.2392156862745098),  # noqa: E501
            "base02": (0.6140350877192983, 0.13286713286713284, 0.2803921568627451),  # noqa: E501
            "base03": (0.6190476190476191, 0.07692307692307696, 0.3568627450980392),  # noqa: E501
            "base04": (0.5952380952380953, 0.07526881720430102, 0.3647058823529412),  # noqa: E501
            "base05": (0.6083333333333334, 0.1351351351351352, 0.7098039215686274),  # noqa: E501
            "base06": (0.6083333333333333, 0.1587301587301586, 0.7529411764705882),  # noqa: E501
            "base07": (0.611111111111111, 0.12244897959183688, 0.807843137254902),  # noqa: E501
            "base08": (0.9870689655172413, 0.651685393258427, 0.6509803921568628),  # noqa: E501
            "base09": (0.08099688473520249, 0.5376884422110553, 0.6098039215686275),  # noqa: E501
            "base0A": (0.10849056603773584, 0.6708860759493671, 0.6901960784313725),  # noqa: E501
            "base0B": (0.26351351351351354, 0.38144329896907214, 0.6196078431372549),  # noqa: E501
            "base0C": (0.5185185185185185, 0.46956521739130436, 0.5490196078431373),  # noqa: E501
            "base0D": (0.5751173708920189, 0.8160919540229885, 0.6588235294117647),  # noqa: E501
            "base0E": (0.7953795379537953, 0.5976331360946747, 0.6686274509803922),  # noqa: E501
            "base0F": (0.013888888888888876, 0.48, 0.5098039215686274),
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

    def test_rgb_to_hsl_and_hsl_to_rgb_correct_type(self):
        test_rgb_colors = self._remove_meta_fields(**self.test_rgb_colors)
        for key, value in test_rgb_colors.items():
            hsl_color = self.test_cls_color.rgb_to_hsl(*value)
            rgb_color = self.test_cls_color.hsl_to_rgb(*hsl_color)
            self.assertIsInstance(hsl_color, tuple)
            self.assertIsInstance(rgb_color, tuple)

    def test_rgb_to_hsl_and_hsl_to_rgb_correct_value(self):
        test_rgb_colors = self._remove_meta_fields(**self.test_rgb_colors)
        for key, value in test_rgb_colors.items():
            benchmark_rgb = value
            benchmark_hsl = self.test_hsl_colors[key]
            hsl_color = self.test_cls_color.rgb_to_hsl(*benchmark_rgb)
            rgb_color = self.test_cls_color.hsl_to_rgb(*hsl_color)
            self.assertEqual(hsl_color, benchmark_hsl)
            self.assertEqual(rgb_color, benchmark_rgb)

    def test_hex_to_hsl_and_hsl_to_hex_returns_correct_type(self):
        test_hex_colors = self._remove_meta_fields(**self.test_hex_colors)
        for key, value in test_hex_colors.items():
            hsl_color = self.test_cls_color.hex_to_hsl(value)
            hex_color = self.test_cls_color.hsl_to_hex(*hsl_color)
            self.assertIsInstance(hsl_color, tuple)
            self.assertIsInstance(hex_color, str)

    def test_hex_to_hsl_and_hsl_to_hex_correct_value(self):
        test_hex_colors = self._remove_meta_fields(**self.test_hex_colors)
        for key, value in test_hex_colors.items():
            benchmark_hex = value
            benchmark_hsl = self.test_hsl_colors[key]
            hsl_color = self.test_cls_color.hex_to_hsl(benchmark_hex)
            hex_color = self.test_cls_color.hsl_to_hex(*hsl_color)
            self.assertEqual(hex_color, benchmark_hex)
            self.assertEqual(hsl_color, benchmark_hsl)

    def test_hue_color(self):
        add_20 = self.test_cls_color.hue('#98c379', 20)
        add_40 = self.test_cls_color.hue('#98c379', 40)
        add_60 = self.test_cls_color.hue('#98c379', 60)
        add_120 = self.test_cls_color.hue('#98c379', 120)

        minus_20 = self.test_cls_color.hue('#98c379', -20)
        minus_40 = self.test_cls_color.hue('#98c379', -40)
        minus_60 = self.test_cls_color.hue('#98c379', -60)
        minus_120 = self.test_cls_color.hue('#98c379', -120)

        self.assertEqual(add_20, '#7fc379')
        self.assertEqual(add_40, '#79c38b')  # there may be an error per 1 byte
        self.assertEqual(add_60, '#79c3a4')
        self.assertEqual(add_120, '#7998c3')

        self.assertEqual(minus_20, '#b1c379')
        self.assertEqual(minus_40, '#c3bd79')
        self.assertEqual(minus_60, '#c3a479')
        self.assertEqual(minus_120, '#c37979')

    def test_saturation_color(self):
        add_20 = self.test_cls_color.saturation('#98c379', 20)
        add_40 = self.test_cls_color.saturation('#98c379', 40)
        add_60 = self.test_cls_color.saturation('#98c379', 60)
        add_120 = self.test_cls_color.saturation('#98c379', 120)

        minus_20 = self.test_cls_color.saturation('#98c379', -20)
        minus_40 = self.test_cls_color.saturation('#98c379', -40)
        minus_60 = self.test_cls_color.saturation('#98c379', -60)
        minus_120 = self.test_cls_color.saturation('#98c379', -120)

        self.assertEqual(add_20, '#95d666')
        self.assertEqual(add_40, '#92ea52')  # there may be an error per 1 byte
        self.assertEqual(add_60, '#8ffd3f')  # there may be an error per 1 byte
        self.assertEqual(add_120, '#8eff3d')

        self.assertEqual(minus_20, '#9bb08c')
        self.assertEqual(minus_40, '#9e9e9e')
        self.assertEqual(minus_60, '#9e9e9e')
        self.assertEqual(minus_120, '#9e9e9e')

    def test_lightness_color(self):
        add_20 = self.test_cls_color.lightness('#98c379', 20)
        add_40 = self.test_cls_color.lightness('#98c379', 40)
        add_60 = self.test_cls_color.lightness('#98c379', 60)
        add_120 = self.test_cls_color.lightness('#98c379', 120)

        minus_20 = self.test_cls_color.lightness('#98c379', -20)
        minus_40 = self.test_cls_color.lightness('#98c379', -40)
        minus_60 = self.test_cls_color.lightness('#98c379', -60)
        minus_120 = self.test_cls_color.lightness('#98c379', -120)

        self.assertEqual(add_20, '#cee3bf')  # there may be an error per 1 byte
        self.assertEqual(add_40, '#ffffff')
        self.assertEqual(add_60, '#ffffff')
        self.assertEqual(add_120, '#ffffff')

        self.assertEqual(minus_20, '#649442')
        self.assertEqual(minus_40, '#354d23')
        self.assertEqual(minus_60, '#050703')
        self.assertEqual(minus_120, '#000000')


class TestСlassColorInternalColorSchemes(unittest.TestCase):

    def setUp(self):
        self.color_schemes = color_schemes
        self.test_cls_color = Color()

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

    def test_rgb_to_hsl_and_hsl_to_rgb_correct_type(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                rgb_color = self.test_cls_color.hex_to_rgb(value)
                hsl_color = self.test_cls_color.rgb_to_hsl(*rgb_color)
                rgb_color = self.test_cls_color.hsl_to_rgb(*hsl_color)
                self.assertIsInstance(hsl_color, tuple)
                self.assertIsInstance(rgb_color, tuple)

    def test_rgb_to_hsl_and_hsl_to_rgb_correct_value(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                benchmark_rgb = self.test_cls_color.hex_to_rgb(value)
                hsl_color = self.test_cls_color.rgb_to_hsl(*benchmark_rgb)
                rgb_color = self.test_cls_color.hsl_to_rgb(*hsl_color)
                self.assertEqual(rgb_color, benchmark_rgb)

    def test_hex_to_hsl_and_hsl_to_hex_returns_correct_type(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                hsl_color = self.test_cls_color.hex_to_hsl(value)
                hex_color = self.test_cls_color.hsl_to_hex(*hsl_color)
                self.assertIsInstance(hsl_color, tuple)
                self.assertIsInstance(hex_color, str)

    def test_hex_to_hsl_and_hsl_to_hex_correct_value(self):
        for color_scheme in self.color_schemes:
            color_scheme = self._remove_meta_fields(**color_scheme)
            for key, value in color_scheme.items():
                benchmark_hex = value
                hsl_color = self.test_cls_color.hex_to_hsl(benchmark_hex)
                hex_color = self.test_cls_color.hsl_to_hex(*hsl_color)
                self.assertEqual(hex_color, benchmark_hex)


if __name__ == "__main__":
    unittest.main()
