############################################################################################################
class GlobalOptions:
    random_seed = None
    summary_freq = 1
    window_height = 1000
    window_width = 1600


############################################################################################################
class World:

    num_rows = 4  # rows x grid size-1 must be < window_height
    num_columns = 8  # columns x grid size-1 must be < window_width
    grid_size = 32  # the width and height of each grid square (in pixels)
    appearance_size = 20  # this is the size of the appearance vector generated for each thing


############################################################################################################
class Terrain:
    num_types = 3  # all edge tiles are made lakes, all interior tiles are made desert
    plains_prob = .6  # then each grid tile has this chance of being made into plains
    lake_prob = .0  # then each grid tile has this chance of being made into lake
    appearance_variance = 0.05  # the probability each feature of a terrain tile's appearance varies from its prototype


############################################################################################################
class Plant:
    appearance_variance = 0.05  # the probability each feature of a plant's appearance varies from its prototype


############################################################################################################
class WorldObject:
    appearance_variance = 0.05  # the probability each feature of an object's appearance varies from its prototype


############################################################################################################
class Animal:
    output_data = False

    appearance_size = 20
    appearance_variance = 0.10

    pregnancy_chance = 1.0
    mutation_rate = 0.01
    gestation_rate = 50
    childhood_length = 100

    attack_strength = 1
    teeth_attack_strength = 20

    metabolism = 1
    pregnant_metabolism = 2

    starvation_rate = 2.0

    allowed_terrain_dict = {'Lake': False,
                            'Plains': True,
                            'Desert': True
                            }

    action_drive_change_dict = {'Rest':      {'Health': 1.0, 'Energy': -0.01, 'Arousal': 0.0},
                                'Attack':    {'Health': 0.0, 'Energy': -0.10, 'Arousal': 0.0},
                                'Eat':       {'Health': 0.0, 'Energy': -0.03, 'Arousal': 0.0},
                                'Procreate': {'Health': 0.0, 'Energy': -0.05, 'Arousal': -20.0},
                                'Turn':      {'Health': 0.1, 'Energy': -0.02, 'Arousal': 0.0},
                                'Move':      {'Health': 0.0, 'Energy': -0.10, 'Arousal': 0.0}}

    # num nucleotides in gene, how converted to value
    trait_gene_size_dict = {'Sex':                      (1, 'binary'),
                            'Max Size':                 (5, 'sum'),
                            'Diet':                     (20, 'mean'),
                            'Teeth':                    (20, 'mean'),
                            'Breathes':                 (10, 'mean'),
                            'Num Hidden Neurons':       (8, 'binary'),
                            'Weight Init Stdev':        (8, 'inv_binary'),
                            'Prediction Learning Rate': (8, 'inv_binary'),
                            'Health Value Direction':   (1, 'direction'),
                            'Health+ Learning Rate':    (8, 'inv_binary'),
                            'Health- Learning Rate':    (8, 'inv_binary'),
                            'HealthD+ Learning Rate':   (8, 'inv_binary'),
                            'HealthD- Learning Rate':   (8, 'inv_binary'),
                            'Energy Value Direction':   (1, 'direction'),
                            'Energy+ Learning Rate':    (8, 'inv_binary'),
                            'Energy- Learning Rate':    (8, 'inv_binary'),
                            'EnergyD+ Learning Rate':   (8, 'inv_binary'),
                            'EnergyD- Learning Rate':   (8, 'inv_binary'),
                            'Arousal Value Direction':  (1, 'direction'),
                            'Arousal+ Learning Rate':   (8, 'inv_binary'),
                            'Arousal- Learning Rate':   (8, 'inv_binary'),
                            'ArousalD+ Learning Rate':  (8, 'inv_binary'),
                            'ArousalD- Learning Rate':  (8, 'inv_binary'),
                            'Rest Bias':                (4, 'sum'),
                            'Attack Bias':              (4, 'sum'),
                            'Eat Bias':                 (4, 'sum'),
                            'Procreate Bias':           (4, 'sum'),
                            'Turn Bias':                (4, 'sum'),
                            'Move Bias':                (4, 'sum'),
                            'Appearance':               (20, 'vector')
                            }


############################################################################################################
class Lion:
    start_number = 0
    diet_dict = {'Meat': True, 'Plants': False}


############################################################################################################
class Zebra:
    start_number = 1
    diet_dict = {'Meat': False, 'Plants': True}