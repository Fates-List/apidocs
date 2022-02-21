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

class StaffRole(object):
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
        'staff_id': 'str',
        'perm': 'int',
        'name': 'str',
        'fname': 'str'
    }

    attribute_map = {
        'id': 'id',
        'staff_id': 'staff_id',
        'perm': 'perm',
        'name': 'name',
        'fname': 'fname'
    }

    def __init__(self, id=None, staff_id=None, perm=None, name='', fname=''):  # noqa: E501
        """StaffRole - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._staff_id = None
        self._perm = None
        self._name = None
        self._fname = None
        self.discriminator = None
        self.id = id
        self.staff_id = staff_id
        self.perm = perm
        if name is not None:
            self.name = name
        if fname is not None:
            self.fname = fname

    @property
    def id(self):
        """Gets the id of this StaffRole.  # noqa: E501


        :return: The id of this StaffRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffRole.


        :param id: The id of this StaffRole.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def staff_id(self):
        """Gets the staff_id of this StaffRole.  # noqa: E501


        :return: The staff_id of this StaffRole.  # noqa: E501
        :rtype: str
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this StaffRole.


        :param staff_id: The staff_id of this StaffRole.  # noqa: E501
        :type: str
        """
        if staff_id is None:
            raise ValueError("Invalid value for `staff_id`, must not be `None`")  # noqa: E501

        self._staff_id = staff_id

    @property
    def perm(self):
        """Gets the perm of this StaffRole.  # noqa: E501


        :return: The perm of this StaffRole.  # noqa: E501
        :rtype: int
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this StaffRole.


        :param perm: The perm of this StaffRole.  # noqa: E501
        :type: int
        """
        if perm is None:
            raise ValueError("Invalid value for `perm`, must not be `None`")  # noqa: E501

        self._perm = perm

    @property
    def name(self):
        """Gets the name of this StaffRole.  # noqa: E501


        :return: The name of this StaffRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffRole.


        :param name: The name of this StaffRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fname(self):
        """Gets the fname of this StaffRole.  # noqa: E501


        :return: The fname of this StaffRole.  # noqa: E501
        :rtype: str
        """
        return self._fname

    @fname.setter
    def fname(self, fname):
        """Sets the fname of this StaffRole.


        :param fname: The fname of this StaffRole.  # noqa: E501
        :type: str
        """

        self._fname = fname

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
        if issubclass(StaffRole, dict):
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
        if not isinstance(other, StaffRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other