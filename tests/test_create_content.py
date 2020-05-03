import json
import unittest

from bootstrap.create_content import create_content_handler


class TestCreateContent(unittest.TestCase):
    @staticmethod
    def get_base_event():
        """
        Sample event from https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html
        :return: dict
        """
        return {
            "requestContext": {
                "elb": {
                    "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/lambda-279XGJDqGZ5rsrHC2Fjr/49e9d65c45c6791a"
                }
            },
            "httpMethod": "GET",
            "path": "/lambda",
            "queryStringParameters": {
                "query": "1234ABCD"
            },
            "headers": {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "accept-encoding": "gzip",
                "accept-language": "en-US,en;q=0.9",
                "connection": "keep-alive",
                "host": "lambda-alb-123578498.us-east-2.elb.amazonaws.com",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                "x-amzn-trace-id": "Root=1-5c536348-3d683b8b04734faae651f476",
                "x-forwarded-for": "72.12.164.125",
                "x-forwarded-port": "80",
                "x-forwarded-proto": "http",
                "x-imforwards": "20"
            },
            "body": "",
            "isBase64Encoded": False
        }

    def test_main(self):
        # given
        event = TestCreateContent.get_base_event()
        context = {"aws_request_id": 1111}  # https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
        # when
        result = create_content_handler(event, context)
        # then
        self.assertEqual(json.loads(result["body"])["message"], "Hello 1234ABCD!")
