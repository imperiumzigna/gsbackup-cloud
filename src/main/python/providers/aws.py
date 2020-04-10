from fbs_runtime.application_context import cached_property
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QSettings
import boto3


def create_session(AWS_KEY, AWS_SECRET, region='us-east-1'):
    session = boto3.Session(AWS_KEY, AWS_SECRET, region)
