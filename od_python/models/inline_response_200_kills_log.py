# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 15.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200KillsLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time': 'int',
        'key': 'str'
    }

    attribute_map = {
        'time': 'time',
        'key': 'key'
    }

    def __init__(self, time=None, key=None):
        """
        InlineResponse200KillsLog - a model defined in Swagger
        """

        self._time = None
        self._key = None

        if time is not None:
          self.time = time
        if key is not None:
          self.key = key

    @property
    def time(self):
        """
        Gets the time of this InlineResponse200KillsLog.
        time

        :return: The time of this InlineResponse200KillsLog.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this InlineResponse200KillsLog.
        time

        :param time: The time of this InlineResponse200KillsLog.
        :type: int
        """

        self._time = time

    @property
    def key(self):
        """
        Gets the key of this InlineResponse200KillsLog.
        key

        :return: The key of this InlineResponse200KillsLog.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this InlineResponse200KillsLog.
        key

        :param key: The key of this InlineResponse200KillsLog.
        :type: str
        """

        self._key = key

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse200KillsLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
