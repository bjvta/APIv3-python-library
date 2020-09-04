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
from sib_api_v3_sdk.models.get_sms_campaign_overview import GetSmsCampaignOverview  # noqa: F401,E501

class GetSmsCampaign(GetSmsCampaignOverview):
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
        'recipients': 'object',
        'statistics': 'object'
    }
    if hasattr(GetSmsCampaignOverview, "swagger_types"):
        swagger_types.update(GetSmsCampaignOverview.swagger_types)

    attribute_map = {
        'recipients': 'recipients',
        'statistics': 'statistics'
    }
    if hasattr(GetSmsCampaignOverview, "attribute_map"):
        attribute_map.update(GetSmsCampaignOverview.attribute_map)

    def __init__(self, recipients=None, statistics=None, *args, **kwargs):  # noqa: E501
        """GetSmsCampaign - a model defined in Swagger"""  # noqa: E501
        self._recipients = None
        self._statistics = None
        self.discriminator = None
        self.recipients = recipients
        self.statistics = statistics
        GetSmsCampaignOverview.__init__(self, *args, **kwargs)

    @property
    def recipients(self):
        """Gets the recipients of this GetSmsCampaign.  # noqa: E501


        :return: The recipients of this GetSmsCampaign.  # noqa: E501
        :rtype: object
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this GetSmsCampaign.


        :param recipients: The recipients of this GetSmsCampaign.  # noqa: E501
        :type: object
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def statistics(self):
        """Gets the statistics of this GetSmsCampaign.  # noqa: E501


        :return: The statistics of this GetSmsCampaign.  # noqa: E501
        :rtype: object
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this GetSmsCampaign.


        :param statistics: The statistics of this GetSmsCampaign.  # noqa: E501
        :type: object
        """
        if statistics is None:
            raise ValueError("Invalid value for `statistics`, must not be `None`")  # noqa: E501

        self._statistics = statistics

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
        if issubclass(GetSmsCampaign, dict):
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
        if not isinstance(other, GetSmsCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
