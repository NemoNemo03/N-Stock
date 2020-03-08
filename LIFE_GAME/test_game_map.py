from unittest import TestCase
from itertools import chain
from itertools import cycle
from unittest import TestCase
from unittest import mock
from game_map import GameMap



class TestGameMap(TestCase):
    def setUp(self):
        self.game_map = GameMap(4, 3)

    def test_init(self):
        self.assertRaises(TypeError, GameMap, ('a', 3))
        self.assertRaises(TypeError, GameMap, (4, 'b'))

    def test_rows(self):
        self.assertEqual(4,self.game_map.rows,"Should get correct rows")


    def test_cols(self):
        self.assertEqual(3, self.game_map.cols, "Should get correct rows")

    @mock.patch('random.random', new=mock.Mock(side_effect=chain(cycle([0.3, 0.6, 0.9]))))
    def test_reset(self):
        self.game_map.reset()
        for i in range(0, 4):
            self.assertEqual(1, self.game_map.get(i, 0))
            for j in range(1, 3):
                self.assertEqual(0, self.game_map.get(i, j))
        self.assertRaises(TypeError, self.game_map.reset, possibility='ab')

    def test_get_set(self):
        self.assertEqual(0, self.game_map.get(0, 0), "Cells init to 0")
        self.game_map.set(0, 0, 1)
        self.assertEqual(1, self.game_map.get(0, 0), "Should get value set by set")
        self.assertRaises(TypeError, self.game_map.get, ("d3d3f", 0))
        self.assertRaises(TypeError, self.game_map.get, (0, 'b'))
        self.assertRaises(TypeError, self.game_map.set, ('a', 0, 1))
        self.assertRaises(TypeError, self.game_map.set, (0, 'b', 1))
        self.assertRaises(TypeError, self.game_map.set, (0, 0, 'c'))

    def test_get_neighbor_count(self):
        expected_value = [[8] * 3] * 4
        self.game_map.cells = [[1] * 3] * 4
        for i in range(0, 4):
            for j in range(0, 3):
                self.assertEqual(expected_value[i][j], self.game_map.get_neighbor_count(i, j), '(%d %d)' % (i, j))
        self.assertRaises(TypeError, self.game_map.get_neighbor_count, ('a', 0))
        self.assertRaises(TypeError, self.game_map.get_neighbor_count, (0, 'b'))

    @mock.patch('game_map.GameMap.get_neighbor_count', new=mock.Mock(return_value=8))
    # game_map.GameMap.get_neighbor_count
    def test_get_neighbor_count_map(self):
        expected_value = [[8] * 3] * 4
        self.assertEqual(expected_value, self.game_map.get_neighbor_count_map())

    def test_set_map(self):
        self.assertRaises(TypeError, self.game_map.set_map, {(0, 0): 1})
        self.assertRaises(AssertionError, self.game_map.set_map, [[1] * 3] * 3)
        self.assertRaises(TypeError, self.game_map.set_map, [['1'] * 3] * 4)
        self.assertRaises(AssertionError, self.game_map.set_map, [[2] * 3] * 4)

        self.game_map.set_map([[1] * 3] * 4)
        self.assertEqual([[1] * 3] * 4, self.game_map.cells)

    def test_print_map(self):
        self.game_map.cells = [
            [0, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        with mock.patch('builtins.print') as mock1:
            self.game_map.print_map()
            mock1.assert_has_calls([
                mock.call('0 1 1'),
                mock.call('0 0 1'),
                mock.call('1 1 1'),
                mock.call('0 0 0'),
            ])


