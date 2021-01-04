import os
from absl import logging, flags

FLAGS = flags.FLAGS

flags.DEFINE_string('listen_addr', '[::]:' + os.getenv('PORT', '50050'), 'Address to listen.')
flags.DEFINE_string('sentry', None, 'Sentry endpoint')
flags.DEFINE_string('port', os.getenv('PORT', ''), '')
