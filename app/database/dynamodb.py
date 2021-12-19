from decimal import Decimal

import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key, Attr

from app.config import settings, logging

logger = logging.getLogger(__name__)


class AbstractTable:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource("dynamodb")
        self.client = boto3.client("dynamodb")
        self.table_name = table_name

        self.table = self.dynamodb.Table(self.table_name)


class Table(AbstractTable):
    def __init__(self, table_name):
        AbstractTable.__init__(self, table_name)

    def filter(self, **kwargs):
        if eval(kwargs["bigger_than"]) is not None:
            filter_corr = Key(kwargs["correlation_type"] + "_corr").gt(
                Decimal(kwargs["bigger_than"])
            )

        if eval(kwargs["smaller_than"]) is not None:
            filter_corr = Key(kwargs["correlation_type"] + "_corr").lt(
                Decimal(kwargs["smaller_than"])
            )

        if kwargs["order_by"] == "DESC":
            ScanIndexForward = False
        else:
            ScanIndexForward = True

        logger.info(f"Sonuç geliyor{self.table_name}")

        response = self.table.query(
            IndexName=f"""{kwargs["correlation_type"]}_corr-index""",
            KeyConditionExpression=Key("date").eq(kwargs["date"]) & filter_corr,
            FilterExpression=Attr("pair").contains(kwargs["contain"]),
            ScanIndexForward=ScanIndexForward,
            ReturnConsumedCapacity="TOTAL",
        )

        logger.info(response)

        return {"data": response["Items"]}
