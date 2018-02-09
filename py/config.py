# hyper params

FILTERS = 32
VALUE_HIDDEN_UNITS = 128
VALUE_LOSS_FACTOR = 1.0
BATCHNORM_MOMENTUM = 0.1  # decay=0.9

WEIGHTS_DIRECTORY = "../weights"

# board
BOARD_SIZE = 15

# train
RECENT_COUNT = 10000
BATCH_SIZE = 256
LEARNING_RATE = 1E-4
WEIGHT_COUNT = 2
WEIGHT_EPOCH = 1

# selfplay
SELFPLAY_PROCESS_COUNT = 5
SELFPLAY_TARGET_ROUNDS = 500

# evaluator
EVAL_PROCESS_COUNT = 5
EVAL_TARGET_ROUNDS = 50