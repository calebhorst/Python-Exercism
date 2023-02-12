def get_rounds(number):
    """
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    list_cuurent_round_plus_next_2 = [number, number+1, number+2]
    return list_cuurent_round_plus_next_2


def concatenate_rounds(rounds_1, rounds_2):
    """
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return float( sum(hand) / len(hand))


def approx_average_is_average(hand):
    """
    # Note: The length of all hands are odd, to make finding a median easier.
    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    # median
    hand.sort()
    mid = len(hand) // 2
    median_val = (hand[mid] + hand[~mid]) / 2
    # avg of first and last cards
    avg_val = (hand[0] + hand[-1]) / 2
    # Return True if either one or both of the strategies result in a number equal to the actual average
    if card_average(hand) == median_val or card_average(hand) == avg_val:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    avg_even = hand[1::2] # list start at 0
    avg_odd = hand[::2]
    sum_even = sum(avg_even) / len(avg_even)
    sum_odd = sum(avg_odd) / len(avg_odd)
    if sum_even == sum_odd:
        return True
    else:
        return False


def maybe_double_last(hand):
    """
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    else:
        return hand
