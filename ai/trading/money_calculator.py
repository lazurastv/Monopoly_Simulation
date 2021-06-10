from ai.logic.sub_logic import SubLogic


class MoneyCalculator(SubLogic):
    MONTE_CARLO_ITER = 10
    simulation = False

    def __init__(self, logic):
        super().__init__(logic)
        self.prices = []

    def load_game(self, graph=None):
        game_copy = self.logic.game.copy()
        if graph:
            unrolled = graph.unroll()
            filled = game_copy.players.fill_unrolled_graph(unrolled)
            game_copy.board.change_owners(filled)
        return game_copy

    def get(self, index):
        return self.prices[index]

    def calculate_prices(self, graphs):
        self.prices = []
        for graph in graphs:
            self.prices.append(self.approximation(graph))

    def verify_trades(self, index, trades):
        target = self.get_player().id
        prices = self.get(index)
        trades.sort(key=lambda x: prices[target][x[0]])
        total = {target: 0}
        for player, _ in trades:
            needed = prices[target][player]
            if needed > 0:
                total[target] += needed
            else:
                total[player] = -needed
        for player in total:
            if not self.logic.game.get_player_by_id(player).has(total[player]):
                return False
        return True

    def approximation(self, graph):
        diffs = self.gains_of_each(graph)
        matrix = {}
        for player_1 in graph:
            matrix[player_1] = {}
            for player_2 in graph:
                matrix[player_1][player_2] = int((diffs[player_1] - diffs[player_2]) / 100)
        return matrix

    def gains_of_each(self, graph):
        diffs = {}
        for player in graph:
            diffs[player] = 0
        unrolled = graph.unroll()
        groups = []
        for owner, tile_index in unrolled:
            tile = self.logic.game.get_tile(tile_index)
            pair = (owner, tile.group)
            if pair not in groups:
                groups.append(pair)
        for owner, group in groups:
            for tile in group:
                for player in graph:
                    if player == owner:
                        diffs[player] += tile.rents[5]
                    else:
                        diffs[player] -= tile.rents[5]
        return diffs

    def monte_carlo(self, graph=None):
        game_copy = self.load_game(graph)
        wins = 0
        MoneyCalculator.simulation = True
        for i in range(MoneyCalculator.MONTE_CARLO_ITER):
            game_instance = game_copy.copy()
            me = game_instance.players.get_by_id(self.logic.player.id)
            game_instance.start()
            if game_instance.winner is me:
                wins += 1
        return wins / MoneyCalculator.MONTE_CARLO_ITER
