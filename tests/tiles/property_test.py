import unittest
from unittest.mock import patch

from tiles.property import Property


class PropertyTest(unittest.TestCase):
    def setUp(self):
        self.tile = Property("Name", 100, 50)

    @patch("gameplay.player.Player")
    @patch("gameplay.player.Player")
    def test_landed_on(self, mock_1, mock_2):
        player_1 = mock_1.return_value
        player_2 = mock_2.return_value
        self.tile.owner = player_1
        self.tile.landed_on_event(player_1, None)
        self.tile.landed_on_event(player_2, None)
        player_1.pay.assert_not_called()
        player_2.pay.assert_called_with(0, player_1)

    @patch("gameplay.player.Player")
    def test_take_mortgage_no_owner(self, mock):
        player = mock.return_value
        self.tile.take_mortgage(player)
        player.earn.assert_not_called()

    @patch("gameplay.player.Player")
    @patch("gameplay.player.Player")
    def test_take_mortgage_not_owner(self, mock_1, mock_2):
        owner = mock_1.return_value
        other = mock_2.return_value
        self.tile.owner = owner
        self.tile.take_mortgage(other)
        other.earn.assert_not_called()

    @patch("gameplay.player.Player")
    def test_take_mortgage_owner(self, mock):
        player = mock.return_value
        self.tile.owner = player
        self.tile.take_mortgage(player)
        player.earn.assert_called()
        self.assertTrue(self.tile.mortgaged)

    @patch("gameplay.player.Player")
    def test_take_mortgage_owner_after_taken(self, mock):
        player = mock.return_value
        self.tile.owner = player
        self.tile.mortgaged = True
        self.tile.take_mortgage(player)
        player.earn.assert_not_called()


if __name__ == '__main__':
    unittest.main()
