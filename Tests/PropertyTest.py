import unittest
from unittest.mock import patch

from Tiles.Property import Property


class PropertyTest(unittest.TestCase):
    @patch("Gameplay.Player.Player")
    @patch("Gameplay.Player.Player")
    def test_landed_on(self, mock_1, mock_2):
        player_1 = mock_1.return_value
        player_2 = mock_2.return_value
        tile = Property("Some", 100, 50, owner=player_1)
        tile.landed_on_event(player_1, None)
        tile.landed_on_event(player_2, None)
        player_1.pay.assert_not_called()
        player_2.pay.assert_called_with(0, player_1)


if __name__ == '__main__':
    unittest.main()
