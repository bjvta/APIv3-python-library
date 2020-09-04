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

class AbTestCampaignResultClickedLinks(object):
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
        'version_a': 'AbTestVersionClicks',
        'version_b': 'AbTestVersionClicks'
    }

    attribute_map = {
        'version_a': 'Version A',
        'version_b': 'Version B'
    }

    def __init__(self, version_a=None, version_b=None):  # noqa: E501
        """AbTestCampaignResultClickedLinks - a model defined in Swagger"""  # noqa: E501
        self._version_a = None
        self._version_b = None
        self.discriminator = None
        self.version_a = version_a
        self.version_b = version_b

    @property
    def version_a(self):
        """Gets the version_a of this AbTestCampaignResultClickedLinks.  # noqa: E501


        :return: The version_a of this AbTestCampaignResultClickedLinks.  # noqa: E501
        :rtype: AbTestVersionClicks
        """
        return self._version_a

    @version_a.setter
    def version_a(self, version_a):
        """Sets the version_a of this AbTestCampaignResultClickedLinks.


        :param version_a: The version_a of this AbTestCampaignResultClickedLinks.  # noqa: E501
        :type: AbTestVersionClicks
        """
        if version_a is None:
            raise ValueError("Invalid value for `version_a`, must not be `None`")  # noqa: E501

        self._version_a = version_a

    @property
    def version_b(self):
        """Gets the version_b of this AbTestCampaignResultClickedLinks.  # noqa: E501


        :return: The version_b of this AbTestCampaignResultClickedLinks.  # noqa: E501
        :rtype: AbTestVersionClicks
        """
        return self._version_b

    @version_b.setter
    def version_b(self, version_b):
        """Sets the version_b of this AbTestCampaignResultClickedLinks.


        :param version_b: The version_b of this AbTestCampaignResultClickedLinks.  # noqa: E501
        :type: AbTestVersionClicks
        """
        if version_b is None:
            raise ValueError("Invalid value for `version_b`, must not be `None`")  # noqa: E501

        self._version_b = version_b

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
        if issubclass(AbTestCampaignResultClickedLinks, dict):
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
        if not isinstance(other, AbTestCampaignResultClickedLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
