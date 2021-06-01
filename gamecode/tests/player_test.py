import unittest
from unittest.mock import patch

from gamecode.gameplay.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_pay_int(self):
        self.player.pay(1200)
        self.assertEqual(self.player.money, 300)

    def test_pay_float(self):
        self.player.pay(1223.723)
        self.assertEqual(self.player.money, 277)

    def test_pay_someone(self):
        player_2 = Player()
        self.player.pay(1000, player_2)
        self.assertEqual(self.player.money, 500)
        self.assertEqual(player_2.money, 2500)

    def test_move(self):
        self.player.move(10)
        self.assertEqual(self.player.position, 10)
        self.player.move(32)
        self.assertEqual(self.player.position, 2)

    def test_not_crossed(self):
        self.player.move(10)
        self.player.crossed_start_bonus()
        self.assertEqual(self.player.money, 1500)

    def test_crossed(self):
        self.player.position = 10
        self.player.move(32)
        self.player.crossed_start_bonus()
        self.assertEqual(self.player.money, 1700)

    def test_crossed_teleport(self):
        self.player.position = 2
        self.player.move_to(1)
        self.player.crossed_start_bonus()
        self.assertEqual(self.player.money, 1700)

    def test_has_money(self):
        self.assertTrue(self.player.has(1000))
        self.assertTrue(self.player.has(1500))
        self.assertFalse(self.player.has(2000))

    @patch("tiles.property.Property")
    @patch("tiles.property.Property")
    def test_has_property(self, mock_1, mock_2):
        tile_a = mock_1.return_value
        tile_b = mock_2.return_value
        self.player.add_property(tile_a)
        self.assertTrue(self.player.has(tile_a))
        self.assertFalse(self.player.has(tile_b))

    @patch("tiles.property.Property")
    def test_connection(self, mock):
        tile = mock.return_value
        self.player.add_property(tile)
        tile.name = "Text"
        self.assertTrue(list(self.player.properties)[0].name == "Text")

    def test_copy(self):
        self.player.money = 2000
        player_copy = self.player.__deepcopy__()
        self.assertEqual(self.player.money, player_copy.money)
        player_copy.money = 2500
        self.assertNotEqual(self.player.money, player_copy.money)


if __name__ == '__main__':
    unittest.main()
