# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """
    Return total amount of prep time.

    This function takes one number representing the number of layers  and calculates the total elapsed minutes spent preparing the     lasagna based on the 2 minutes per layer.
    """
    return PREPARATION_TIME * number_of_layers
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    total_elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_elapsed_time_in_minutes