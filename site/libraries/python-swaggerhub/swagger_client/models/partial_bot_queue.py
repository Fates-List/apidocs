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

class PartialBotQueue(object):
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
        'user': 'AllOfPartialBotQueueUser',
        'prefix': 'str',
        'invite': 'str',
        'description': 'str',
        'state': 'BotState',
        'guild_count': 'int',
        'votes': 'int',
        'long_description': 'str',
        'website': 'str',
        'support': 'str',
        'owners': 'list[FilteredBotOwner]',
        'tags': 'list[FilteredBotTag]'
    }

    attribute_map = {
        'user': 'user',
        'prefix': 'prefix',
        'invite': 'invite',
        'description': 'description',
        'state': 'state',
        'guild_count': 'guild_count',
        'votes': 'votes',
        'long_description': 'long_description',
        'website': 'website',
        'support': 'support',
        'owners': 'owners',
        'tags': 'tags'
    }

    def __init__(self, user=None, prefix=None, invite=None, description=None, state=None, guild_count=None, votes=None, long_description=None, website=None, support=None, owners=None, tags=None):  # noqa: E501
        """PartialBotQueue - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._prefix = None
        self._invite = None
        self._description = None
        self._state = None
        self._guild_count = None
        self._votes = None
        self._long_description = None
        self._website = None
        self._support = None
        self._owners = None
        self._tags = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if prefix is not None:
            self.prefix = prefix
        self.invite = invite
        self.description = description
        self.state = state
        self.guild_count = guild_count
        self.votes = votes
        self.long_description = long_description
        if website is not None:
            self.website = website
        if support is not None:
            self.support = support
        self.owners = owners
        self.tags = tags

    @property
    def user(self):
        """Gets the user of this PartialBotQueue.  # noqa: E501


        :return: The user of this PartialBotQueue.  # noqa: E501
        :rtype: AllOfPartialBotQueueUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PartialBotQueue.


        :param user: The user of this PartialBotQueue.  # noqa: E501
        :type: AllOfPartialBotQueueUser
        """

        self._user = user

    @property
    def prefix(self):
        """Gets the prefix of this PartialBotQueue.  # noqa: E501


        :return: The prefix of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this PartialBotQueue.


        :param prefix: The prefix of this PartialBotQueue.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def invite(self):
        """Gets the invite of this PartialBotQueue.  # noqa: E501


        :return: The invite of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._invite

    @invite.setter
    def invite(self, invite):
        """Sets the invite of this PartialBotQueue.


        :param invite: The invite of this PartialBotQueue.  # noqa: E501
        :type: str
        """
        if invite is None:
            raise ValueError("Invalid value for `invite`, must not be `None`")  # noqa: E501

        self._invite = invite

    @property
    def description(self):
        """Gets the description of this PartialBotQueue.  # noqa: E501


        :return: The description of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PartialBotQueue.


        :param description: The description of this PartialBotQueue.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def state(self):
        """Gets the state of this PartialBotQueue.  # noqa: E501


        :return: The state of this PartialBotQueue.  # noqa: E501
        :rtype: BotState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PartialBotQueue.


        :param state: The state of this PartialBotQueue.  # noqa: E501
        :type: BotState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def guild_count(self):
        """Gets the guild_count of this PartialBotQueue.  # noqa: E501


        :return: The guild_count of this PartialBotQueue.  # noqa: E501
        :rtype: int
        """
        return self._guild_count

    @guild_count.setter
    def guild_count(self, guild_count):
        """Sets the guild_count of this PartialBotQueue.


        :param guild_count: The guild_count of this PartialBotQueue.  # noqa: E501
        :type: int
        """
        if guild_count is None:
            raise ValueError("Invalid value for `guild_count`, must not be `None`")  # noqa: E501

        self._guild_count = guild_count

    @property
    def votes(self):
        """Gets the votes of this PartialBotQueue.  # noqa: E501


        :return: The votes of this PartialBotQueue.  # noqa: E501
        :rtype: int
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this PartialBotQueue.


        :param votes: The votes of this PartialBotQueue.  # noqa: E501
        :type: int
        """
        if votes is None:
            raise ValueError("Invalid value for `votes`, must not be `None`")  # noqa: E501

        self._votes = votes

    @property
    def long_description(self):
        """Gets the long_description of this PartialBotQueue.  # noqa: E501


        :return: The long_description of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this PartialBotQueue.


        :param long_description: The long_description of this PartialBotQueue.  # noqa: E501
        :type: str
        """
        if long_description is None:
            raise ValueError("Invalid value for `long_description`, must not be `None`")  # noqa: E501

        self._long_description = long_description

    @property
    def website(self):
        """Gets the website of this PartialBotQueue.  # noqa: E501


        :return: The website of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PartialBotQueue.


        :param website: The website of this PartialBotQueue.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def support(self):
        """Gets the support of this PartialBotQueue.  # noqa: E501


        :return: The support of this PartialBotQueue.  # noqa: E501
        :rtype: str
        """
        return self._support

    @support.setter
    def support(self, support):
        """Sets the support of this PartialBotQueue.


        :param support: The support of this PartialBotQueue.  # noqa: E501
        :type: str
        """

        self._support = support

    @property
    def owners(self):
        """Gets the owners of this PartialBotQueue.  # noqa: E501


        :return: The owners of this PartialBotQueue.  # noqa: E501
        :rtype: list[FilteredBotOwner]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this PartialBotQueue.


        :param owners: The owners of this PartialBotQueue.  # noqa: E501
        :type: list[FilteredBotOwner]
        """
        if owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def tags(self):
        """Gets the tags of this PartialBotQueue.  # noqa: E501


        :return: The tags of this PartialBotQueue.  # noqa: E501
        :rtype: list[FilteredBotTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PartialBotQueue.


        :param tags: The tags of this PartialBotQueue.  # noqa: E501
        :type: list[FilteredBotTag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if issubclass(PartialBotQueue, dict):
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
        if not isinstance(other, PartialBotQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other