import logging
import watchtower

#############################################################################
############################# LOGGER UTIL ####################################
#############################################################################

################## Requirements ######################################
# Need to have a log_group already created
# stream will be generated automatically by the library
# Below permissions are required for ec2 instance
# "logs:CreateLogGroup"
# "logs:CreateLogStream",
# "logs:PutLogEvents"

class Logger():
     def __init__(self, **kwargs) -> None:
          logging.basicConfig(level=logging.INFO)
          logger_name = kwargs["logger_name"]
          logger = logging.getLogger(logger_name)
          
          handler = watchtower.CloudWatchLogHandler(
               log_group = kwargs["log_group_name"],
               stream_name = "{logger_name}-{strftime:%Y-%m-%d} [{strftime:%H.%M.%S UTC}]",
               create_log_group = True,
          )

          logger.addHandler(handler)
          self.logger = logger

     def get_logger(self):
          return self.logger

################## Usage Example ######################################
# logger = Logger(
#      logger_name = "test",
#      log_group_name = "my-lg-grp"
# ).get_logger()
#
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")