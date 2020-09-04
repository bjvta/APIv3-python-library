# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetChildInfoApiKeys(object):
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
        'v2': 'list[GetChildInfoApiKeysV2]',
        'v3': 'list[GetChildInfoApiKeysV3]'
    }

    attribute_map = {
        'v2': 'v2',
        'v3': 'v3'
    }

    def __init__(self, v2=None, v3=None):  # noqa: E501
        """GetChildInfoApiKeys - a model defined in Swagger"""  # noqa: E501
        self._v2 = None
        self._v3 = None
        self.discriminator = None
        self.v2 = v2
        if v3 is not None:
            self.v3 = v3

    @property
    def v2(self):
        """Gets the v2 of this GetChildInfoApiKeys.  # noqa: E501


        :return: The v2 of this GetChildInfoApiKeys.  # noqa: E501
        :rtype: list[GetChildInfoApiKeysV2]
        """
        return self._v2

    @v2.setter
    def v2(self, v2):
        """Sets the v2 of this GetChildInfoApiKeys.


        :param v2: The v2 of this GetChildInfoApiKeys.  # noqa: E501
        :type: list[GetChildInfoApiKeysV2]
        """
        if v2 is None:
            raise ValueError("Invalid value for `v2`, must not be `None`")  # noqa: E501

        self._v2 = v2

    @property
    def v3(self):
        """Gets the v3 of this GetChildInfoApiKeys.  # noqa: E501


        :return: The v3 of this GetChildInfoApiKeys.  # noqa: E501
        :rtype: list[GetChildInfoApiKeysV3]
        """
        return self._v3

    @v3.setter
    def v3(self, v3):
        """Sets the v3 of this GetChildInfoApiKeys.


        :param v3: The v3 of this GetChildInfoApiKeys.  # noqa: E501
        :type: list[GetChildInfoApiKeysV3]
        """

        self._v3 = v3

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
        if issubclass(GetChildInfoApiKeys, dict):
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
        if not isinstance(other, GetChildInfoApiKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
