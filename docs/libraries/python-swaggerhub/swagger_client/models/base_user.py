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

class BaseUser(object):
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
        'id': 'str',
        'username': 'str',
        'avatar': 'str',
        'disc': 'str',
        'status': 'AllOfBaseUserStatus',
        'bot': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'avatar': 'avatar',
        'disc': 'disc',
        'status': 'status',
        'bot': 'bot'
    }

    def __init__(self, id='0', username='Unknown User', avatar='https://fateslist.xyz/static/botlisticon.webp', disc='0000', status=None, bot=True):  # noqa: E501
        """BaseUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._avatar = None
        self._disc = None
        self._status = None
        self._bot = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if avatar is not None:
            self.avatar = avatar
        if disc is not None:
            self.disc = disc
        if status is not None:
            self.status = status
        if bot is not None:
            self.bot = bot

    @property
    def id(self):
        """Gets the id of this BaseUser.  # noqa: E501


        :return: The id of this BaseUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseUser.


        :param id: The id of this BaseUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this BaseUser.  # noqa: E501


        :return: The username of this BaseUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this BaseUser.


        :param username: The username of this BaseUser.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def avatar(self):
        """Gets the avatar of this BaseUser.  # noqa: E501


        :return: The avatar of this BaseUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this BaseUser.


        :param avatar: The avatar of this BaseUser.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def disc(self):
        """Gets the disc of this BaseUser.  # noqa: E501


        :return: The disc of this BaseUser.  # noqa: E501
        :rtype: str
        """
        return self._disc

    @disc.setter
    def disc(self, disc):
        """Sets the disc of this BaseUser.


        :param disc: The disc of this BaseUser.  # noqa: E501
        :type: str
        """

        self._disc = disc

    @property
    def status(self):
        """Gets the status of this BaseUser.  # noqa: E501


        :return: The status of this BaseUser.  # noqa: E501
        :rtype: AllOfBaseUserStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseUser.


        :param status: The status of this BaseUser.  # noqa: E501
        :type: AllOfBaseUserStatus
        """

        self._status = status

    @property
    def bot(self):
        """Gets the bot of this BaseUser.  # noqa: E501


        :return: The bot of this BaseUser.  # noqa: E501
        :rtype: bool
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this BaseUser.


        :param bot: The bot of this BaseUser.  # noqa: E501
        :type: bool
        """

        self._bot = bot

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
        if issubclass(BaseUser, dict):
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
        if not isinstance(other, BaseUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other