# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sib_api_v3_sdk.models.create_sender_ips import CreateSenderIps  # noqa: F401,E501


class CreateSender(object):
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
        'name': 'str',
        'email': 'str',
        'ips': 'list[CreateSenderIps]'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'ips': 'ips'
    }

    def __init__(self, name=None, email=None, ips=None):  # noqa: E501
        """CreateSender - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._email = None
        self._ips = None
        self.discriminator = None

        self.name = name
        self.email = email
        if ips is not None:
            self.ips = ips

    @property
    def name(self):
        """Gets the name of this CreateSender.  # noqa: E501

        From Name to use for the sender  # noqa: E501

        :return: The name of this CreateSender.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSender.

        From Name to use for the sender  # noqa: E501

        :param name: The name of this CreateSender.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this CreateSender.  # noqa: E501

        From Email to use for the sender  # noqa: E501

        :return: The email of this CreateSender.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateSender.

        From Email to use for the sender  # noqa: E501

        :param email: The email of this CreateSender.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def ips(self):
        """Gets the ips of this CreateSender.  # noqa: E501

        Mandatory in case of dedicated IP, IPs to associate to the sender  # noqa: E501

        :return: The ips of this CreateSender.  # noqa: E501
        :rtype: list[CreateSenderIps]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this CreateSender.

        Mandatory in case of dedicated IP, IPs to associate to the sender  # noqa: E501

        :param ips: The ips of this CreateSender.  # noqa: E501
        :type: list[CreateSenderIps]
        """

        self._ips = ips

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
