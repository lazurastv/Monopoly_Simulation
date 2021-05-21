import unittest
from unittest.mock import patch

from Gameplay.Player import Player


class PlayerTest(unittest.TestCase):
    def test_pay_int(self):
        player = Player()
        player.pay(1200)
        self.assertEqual(player.money, 300)

    def test_pay_float(self):
        player = Player()
        player.pay(1223.723)
        self.assertEqual(player.money, 277)

    def test_pay_someone(self):
        player_1 = Player()
        player_2 = Player()
        player_1.pay(1000, player_2)
        self.assertEqual(player_1.money, 500)
        self.assertEqual(player_2.money, 2500)

    def test_move(self):
        player = Player()
        player.move(10)
        self.assertEqual(player.position, 10)
        player.move(32)
        self.assertEqual(player.position, 2)

    def test_not_crossed(self):
        player = Player()
        player.move(10)
        player.crossed_start_bonus()
        self.assertEqual(player.money, 1500)

    def test_crossed(self):
        player = Player(position=10)
        player.move(32)
        player.crossed_start_bonus()
        self.assertEqual(player.money, 1700)

    def test_crossed_teleport(self):
        player = Player(position=2)
        player.move_to(1)
        player.crossed_start_bonus()
        self.assertEqual(player.money, 1700)

    def test_has_money(self):
        player = Player()
        self.assertTrue(player.has_money(1000))
        self.assertTrue(player.has_money(1500))
        self.assertFalse(player.has_money(2000))

    @patch("Tiles.Property.Property")
    @patch("Tiles.Property.Property")
    def test_has_property(self, mock_1, mock_2):
        tile_a = mock_1.return_value
        tile_b = mock_2.return_value
        player = Player(properties=[tile_a])
        self.assertTrue(player.has_property(tile_a))
        self.assertFalse(player.has_property(tile_b))

    @patch("Tiles.Property.Property")
    def test_connection(self, mock):
        tile = mock.return_value
        player = Player(properties=[tile])
        tile.name = "Text"
        self.assertEqual("Text", player.properties[0].name)


if __name__ == '__main__':
    unittest.main()
