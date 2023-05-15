class Table:
    pass

class BettingStrategy:
    pass

class GameStrategy:
    pass

class Player:
    def __init__(
        self,
        table: Table,
        bet_strategy: BettingStrategy,
        game_strategy: GameStrategy
        ) -> None:
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table

    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table.get_hand()
        if self.table.can_insure(self.hand):
            if self.game_strategy.insurance(self.hand):
                self.table.insure(self.bet_strategy.bet())
                ...


# table = Table()
# flat_bet = Flat()
# dumb = GameStrategy()
# p = Player(table, flat_bet, dumb)
# p.game()

# vs


class Player2:
    def __init__(self, **kw) -> None:
        '''Must provide table, bet_strategy, game_strategy'''
        self.bet_strategy: BettingStrategy = kw['bet_strategy']
        self.game_strategy: GameStrategy = kw['game_strategy']
        self.table: Table = kw['table']

    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table.get_hand()
        if self.table.can_insure(self.hand):
            if self.game_strategy.insurance(self.hand):
                self.table.insure(self.bet_strategy.bet())
                ...
