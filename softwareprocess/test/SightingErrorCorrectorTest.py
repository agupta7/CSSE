import softwareprocess.SightingErrorCorrector as SEC
import unittest

class SightingErrorCorrectorTest(unittest):

# ---- 100 Acceptance tests
# ---- constructor
#------- input :    lat         - 'XdY.Y' format like elsewhere.  -90 < lat < 90
#------             long        - 'XdY.Y' format like elsewhere.  0<= long < 360
#-------            altitude    - 'XdY.Y' format like elsewhere.  0 < alt < 90
#-------            assumedLat  - 'XdY.Y' format like elsewhere.  -90 < lat < 90
#-------            assumedLong - 'XdY.Y' format like elsewhere.  0 <= lat < 360
#------  output   : instance of SightingErrorCorrector
#--------- Happy path analysis
# ----   input : nominal inputs ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ----   input : high inputs ('89d59.9' lat, '359d59.9' long, '89d59.9' altitude, '89d59.9' assumedLat, '359d59.9' assumedLong)
# ----  input : low inputs ('-89d59.9' lat, '0d0.0' long, '0d0.1' altitude, '-89d59.9' assumedLat, '0d0.0' assumedLong)
# ---------Sad path analysis
#-------- input : one of the arguments is too high
#------------------lat too high ('90d0.0' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------long too high ('16d32.3' lat, '360d0.0' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------altitude too high ('16d32.3' lat, '95d41.6' long, '90d0.0' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------assumedLat too high ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '90d0.0' assumedLat, '74d35.3' assumedLong)
# ------------------assumedLong too high ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '360d0.0' assumedLong)
#--------output : ValueError raised explaining which value was too high
#------- input : one of the parameters is too low
#-----------------lat is too low ('-90d0.0' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------long is too low ('16d32.3' lat, '-0d0.1' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------altitude is too low ('16d32.3' lat, '95d41.6' long, '0d0.0' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------assumedLat is too low ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-90d0.0' assumedLat, '74d35.3' assumedLong)
#-----------------assumedLong is too low ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '-0d0.1' assumedLong)
#------ output : ValueError raised explaining which value was too low
