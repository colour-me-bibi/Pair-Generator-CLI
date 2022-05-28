import unittest

from pair_gen import split_at_index, generate_rotations, generate_pairings


class TestPairGen(unittest.TestCase):
    def test_split_at_index(self):
        self.assertEqual(split_at_index(["a", "b", "c", "d"], 0), (
            [],
            ["a", "b", "c", "d"],
        ))
        self.assertEqual(split_at_index(["a", "b", "c", "d"], 1), (
            ["a"],
            ["b", "c", "d"],
        ))
        self.assertEqual(split_at_index(["a", "b", "c", "d"], 2), (
            ["a", "b"],
            ["c", "d"],
        ))
        self.assertEqual(split_at_index(["a", "b", "c", "d"], 3), (
            ["a", "b", "c"],
            ["d"],
        ))
        self.assertEqual(split_at_index(["a", "b", "c", "d"], 4), (
            ["a", "b", "c", "d"],
            [],
        ))
        self.assertNotEqual(split_at_index(["a", "b", "c", "d"], 1), (
            ["a", "b"],
            ["c", "d"],
            ["a", "b"],
        ))

    def test_generate_rotations(self):
        self.assertEqual(list(generate_rotations(["a", "b", "c", "d"])), [
            ["a", "b", "c", "d"],
            ["b", "c", "d", "a"],
            ["c", "d", "a", "b"],
            ["d", "a", "b", "c"],
        ])
        self.assertNotEqual(list(generate_rotations(["a", "b", "c", "d"])), [
            ["a", "b", "c", "d"],
            ["b", "c", "d", "a"],
            ["c", "d", "a", "b"],
            ["d", "a", "b", "c"],
            ["a", "b", "c", "d"],
        ])

    def test_generate_pairings(self):
        self.assertEqual(list(generate_pairings(["a", "b", "c", "d"])), [
            [
                ("a", "d"),
                ("b", "c")
            ],
            [
                ("a", "b"),
                ("c", "d")
            ],
            [
                ("a", "c"),
                ("d", "b"),
            ],
        ])
        self.assertNotEqual(list(generate_pairings(["a", "b", "c", "d"])), [
            [
                ("a", "b"),
                ("c", "d"),
            ],
            [
                ("a", "c"),
                ("b", "d"),
            ],
            [
                ("a", "b"),
                ("b", "d"),
            ],
        ])
