#!/usr/bin/env python
import sys; sys.path.append("..")
import logging
import random
from fireplace.cards.heroes import *
from fireplace.game import Game
from fireplace.player import Player
from fireplace.utils import random_draft


logging.getLogger().setLevel(logging.DEBUG)


def main():
	deck1 = random_draft(hero=MAGE)
	deck2 = random_draft(hero=WARRIOR)
	player1 = Player(name="Player1")
	player1.prepare_deck(deck1, MAGE)
	player2 = Player(name="Player2")
	player2.prepare_deck(deck2, WARRIOR)

	game = Game(players=(player1, player2))
	game.start()

	while True:
		heropower = game.current_player.hero.power
		# always play the hero power, just for kicks
		if heropower.is_playable():
			if heropower.has_target():
				heropower.play(target=random.choice(heropower.targets))
			else:
				heropower.play()
		# iterate over our hand and play whatever is playable
		for card in game.current_player.hand:
			if card.is_playable():
				if card.has_target():
					card.play(target=random.choice(card.targets))
				else:
					card.play()
			else:
				print("Not playing", card)

		# Randomly attack with whatever can attack
		for character in game.current_player.characters:
			if character.can_attack():
				character.attack(random.choice(character.targets))

		game.end_turn()


if __name__ == "__main__":
	main()
