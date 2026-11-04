import unittest

from game import (
    new_game,
    available_moves,
    move_player,
    pickup_item,
    can_cross_bridge,
    can_light_beacon,
    light_beacon,
    is_win,
    is_loss,
)


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Vic")

    def test_new_game_starts_at_beach(self):
        self.assertEqual(self.player["location"], "Beach")

    def test_new_game_starts_with_five_energy(self):
        self.assertEqual(self.player["energy"], 5)

    def test_new_game_inventory_is_empty(self):
        self.assertEqual(self.player["inventory"], [])

    def test_invalid_move_does_not_change_location(self):
        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_valid_move_reduces_energy(self):
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_cannot_move_to_wrong_destination(self):
        success, message = move_player(self.player, "Lighthouse")

        self.assertFalse(success)

    def test_rope_can_be_collected(self):
        move_player(self.player, "Jungle")
        success, message = pickup_item(self.player)

        self.assertTrue(success)
        self.assertIn("Rope", self.player["inventory"])

    def test_cannot_cross_bridge_without_rope(self):
        move_player(self.player, "Jungle")
        move_player(self.player, "Cave")

        success, message = move_player(self.player, "Old Bridge")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Cave")

    def test_can_cross_bridge_with_rope(self):
        move_player(self.player, "Jungle")
        pickup_item(self.player)
        move_player(self.player, "Cave")

        success, message = move_player(self.player, "Old Bridge")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Old Bridge")

    def test_cannot_light_beacon_without_lantern(self):
        self.player["location"] = "Lighthouse"

        success, message = light_beacon(self.player)

        self.assertFalse(success)
        self.assertFalse(is_win(self.player))

    def test_can_win_with_lantern_at_lighthouse(self):
        self.player["location"] = "Lighthouse"
        self.player["inventory"].append("Lantern")

        success, message = light_beacon(self.player)

        self.assertTrue(success)
        self.assertTrue(is_win(self.player))

    def test_running_out_of_energy_causes_loss(self):
        self.player["energy"] = 1

        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertTrue(is_loss(self.player))

    def test_cannot_move_after_game_over(self):
        self.player["game_over"] = True

        success, message = move_player(self.player, "Jungle")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")

    def test_lantern_can_be_collected(self):
        move_player(self.player, "Jungle")
        pickup_item(self.player)
        move_player(self.player, "Cave")

        success, message = pickup_item(self.player)

        self.assertTrue(success)
        self.assertIn("Lantern", self.player["inventory"])

    def test_available_moves_from_beach(self):
        self.assertEqual(available_moves(self.player), ["Jungle"])

    def test_can_cross_bridge_checks_inventory(self):
        self.assertFalse(can_cross_bridge(self.player))

        self.player["inventory"].append("Rope")

        self.assertTrue(can_cross_bridge(self.player))

    def test_can_light_beacon_requires_lantern_and_location(self):
        self.assertFalse(can_light_beacon(self.player))

        self.player["location"] = "Lighthouse"
        self.assertFalse(can_light_beacon(self.player))

        self.player["inventory"].append("Lantern")
        self.assertTrue(can_light_beacon(self.player))


if __name__ == "__main__":
    unittest.main()
