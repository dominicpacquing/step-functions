from datetime import datetime
from uuid import uuid4

import logging
import traceback
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    try:
        logger.info(event)
        # Mocked result
        transaction_result = {
            "id": str(uuid4()),  # Unique ID for the transaction
            "description": "processor",
            "timestamp": datetime.now().isoformat()  # Timestamp of the when the transaction was completed
        }

        return transaction_result

    except Exception as exp:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)

