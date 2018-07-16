new_actions = ['place_street_road','increase_workforce','sell_images','won_level', 'place_market']
#actions_stream comes in via rest
action_stream = ['place_street_road','increase_workforce','sell_images','won_level','place_street_road', 'place_market','increase_workforce']
latency=0.05
threshold=0.5
noise=0.0
baseNoise=0.0
decay=0.5
limit=None
chunk_activations = {}
fired_actions = {}