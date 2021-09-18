import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key

from config import settings, logging

logger = logging.getLogger(__name__)


class AbstractTable:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource(
            "dynamodb", config=Config(read_timeout=585, connect_timeout=585)
        )
        self.client = boto3.client("dynamodb")
        self.table_name = table_name

        self.table = self.dynamodb.Table(self.table_name)


class Table(AbstractTable):
    def __init__(self, table_name):
        AbstractTable.__init__(self, table_name)

    def filter(self, **kwargs):
        if kwargs["bigger_than"] is not None:
            filter_corr = Key(kwargs["correlation_type"] + "_corr").gt(
                str(kwargs["bigger_than"])
            )

        if kwargs["smaller_than"] is not None:
            filter_corr = Key(kwargs["correlation_type"] + "_corr").lt(
                kwargs["smaller_than"]
            )

        if kwargs["order_by"] == "DESC":
            ScanIndexForward = False
        else:
            ScanIndexForward = True

        try:
            limit = int(kwargs["limit"])
        except:
            logger.error("You must enter an integer as limit")

        response = self.table.query(
            IndexName=f"""{kwargs["correlation_type"]}_corr-index""",
            KeyConditionExpression=Key("date").eq("2021-09-16") & filter_corr,
            ScanIndexForward=ScanIndexForward,
            ReturnConsumedCapacity="TOTAL",
            Limit=limit,
        )

        return response["Items"]
