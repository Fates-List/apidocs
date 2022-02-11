# coding: utf-8

"""
    Fates List

                 Current API: v2 beta 3             Default API: v2             API URL: https://api.fateslist.xyz             API Docs: https://apidocs.fateslist.xyz             Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen           # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class APIResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'done': 'bool',
        'reason': 'str'
    }

    attribute_map = {
        'done': 'done',
        'reason': 'reason'
    }

    def __init__(self, done=None, reason=None):  # noqa: E501
        """APIResponse - a model defined in Swagger"""  # noqa: E501
        self._done = None
        self._reason = None
        self.discriminator = None
        self.done = done
        if reason is not None:
            self.reason = reason

    @property
    def done(self):
        """Gets the done of this APIResponse.  # noqa: E501


        :return: The done of this APIResponse.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this APIResponse.


        :param done: The done of this APIResponse.  # noqa: E501
        :type: bool
        """
        if done is None:
            raise ValueError("Invalid value for `done`, must not be `None`")  # noqa: E501

        self._done = done

    @property
    def reason(self):
        """Gets the reason of this APIResponse.  # noqa: E501


        :return: The reason of this APIResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this APIResponse.


        :param reason: The reason of this APIResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(APIResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APIResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
