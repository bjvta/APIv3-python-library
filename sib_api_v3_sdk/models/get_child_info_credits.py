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


class GetChildInfoCredits(object):
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
        'email_credits': 'int',
        'sms_credits': 'int'
    }

    attribute_map = {
        'email_credits': 'emailCredits',
        'sms_credits': 'smsCredits'
    }

    def __init__(self, email_credits=None, sms_credits=None):  # noqa: E501
        """GetChildInfoCredits - a model defined in Swagger"""  # noqa: E501

        self._email_credits = None
        self._sms_credits = None
        self.discriminator = None

        if email_credits is not None:
            self.email_credits = email_credits
        if sms_credits is not None:
            self.sms_credits = sms_credits

    @property
    def email_credits(self):
        """Gets the email_credits of this GetChildInfoCredits.  # noqa: E501

        Email credits available for your child  # noqa: E501

        :return: The email_credits of this GetChildInfoCredits.  # noqa: E501
        :rtype: int
        """
        return self._email_credits

    @email_credits.setter
    def email_credits(self, email_credits):
        """Sets the email_credits of this GetChildInfoCredits.

        Email credits available for your child  # noqa: E501

        :param email_credits: The email_credits of this GetChildInfoCredits.  # noqa: E501
        :type: int
        """

        self._email_credits = email_credits

    @property
    def sms_credits(self):
        """Gets the sms_credits of this GetChildInfoCredits.  # noqa: E501

        SMS credits available for your child  # noqa: E501

        :return: The sms_credits of this GetChildInfoCredits.  # noqa: E501
        :rtype: int
        """
        return self._sms_credits

    @sms_credits.setter
    def sms_credits(self, sms_credits):
        """Sets the sms_credits of this GetChildInfoCredits.

        SMS credits available for your child  # noqa: E501

        :param sms_credits: The sms_credits of this GetChildInfoCredits.  # noqa: E501
        :type: int
        """

        self._sms_credits = sms_credits

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
        if not isinstance(other, GetChildInfoCredits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
