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

class GetTransacSmsReportReports(object):
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
        '_date': 'date',
        'requests': 'int',
        'delivered': 'int',
        'hard_bounces': 'int',
        'soft_bounces': 'int',
        'blocked': 'int',
        'unsubscribed': 'int',
        'replied': 'int',
        'accepted': 'int',
        'rejected': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'requests': 'requests',
        'delivered': 'delivered',
        'hard_bounces': 'hardBounces',
        'soft_bounces': 'softBounces',
        'blocked': 'blocked',
        'unsubscribed': 'unsubscribed',
        'replied': 'replied',
        'accepted': 'accepted',
        'rejected': 'rejected'
    }

    def __init__(self, _date=None, requests=None, delivered=None, hard_bounces=None, soft_bounces=None, blocked=None, unsubscribed=None, replied=None, accepted=None, rejected=None):  # noqa: E501
        """GetTransacSmsReportReports - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._requests = None
        self._delivered = None
        self._hard_bounces = None
        self._soft_bounces = None
        self._blocked = None
        self._unsubscribed = None
        self._replied = None
        self._accepted = None
        self._rejected = None
        self.discriminator = None
        self._date = _date
        self.requests = requests
        self.delivered = delivered
        self.hard_bounces = hard_bounces
        self.soft_bounces = soft_bounces
        self.blocked = blocked
        self.unsubscribed = unsubscribed
        self.replied = replied
        self.accepted = accepted
        self.rejected = rejected

    @property
    def _date(self):
        """Gets the _date of this GetTransacSmsReportReports.  # noqa: E501

        Date for which statistics are retrieved  # noqa: E501

        :return: The _date of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetTransacSmsReportReports.

        Date for which statistics are retrieved  # noqa: E501

        :param _date: The _date of this GetTransacSmsReportReports.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def requests(self):
        """Gets the requests of this GetTransacSmsReportReports.  # noqa: E501

        Number of requests for the date  # noqa: E501

        :return: The requests of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this GetTransacSmsReportReports.

        Number of requests for the date  # noqa: E501

        :param requests: The requests of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if requests is None:
            raise ValueError("Invalid value for `requests`, must not be `None`")  # noqa: E501

        self._requests = requests

    @property
    def delivered(self):
        """Gets the delivered of this GetTransacSmsReportReports.  # noqa: E501

        Number of delivered SMS for the date  # noqa: E501

        :return: The delivered of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this GetTransacSmsReportReports.

        Number of delivered SMS for the date  # noqa: E501

        :param delivered: The delivered of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if delivered is None:
            raise ValueError("Invalid value for `delivered`, must not be `None`")  # noqa: E501

        self._delivered = delivered

    @property
    def hard_bounces(self):
        """Gets the hard_bounces of this GetTransacSmsReportReports.  # noqa: E501

        Number of hardbounces for the date  # noqa: E501

        :return: The hard_bounces of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._hard_bounces

    @hard_bounces.setter
    def hard_bounces(self, hard_bounces):
        """Sets the hard_bounces of this GetTransacSmsReportReports.

        Number of hardbounces for the date  # noqa: E501

        :param hard_bounces: The hard_bounces of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if hard_bounces is None:
            raise ValueError("Invalid value for `hard_bounces`, must not be `None`")  # noqa: E501

        self._hard_bounces = hard_bounces

    @property
    def soft_bounces(self):
        """Gets the soft_bounces of this GetTransacSmsReportReports.  # noqa: E501

        Number of softbounces for the date  # noqa: E501

        :return: The soft_bounces of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._soft_bounces

    @soft_bounces.setter
    def soft_bounces(self, soft_bounces):
        """Sets the soft_bounces of this GetTransacSmsReportReports.

        Number of softbounces for the date  # noqa: E501

        :param soft_bounces: The soft_bounces of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if soft_bounces is None:
            raise ValueError("Invalid value for `soft_bounces`, must not be `None`")  # noqa: E501

        self._soft_bounces = soft_bounces

    @property
    def blocked(self):
        """Gets the blocked of this GetTransacSmsReportReports.  # noqa: E501

        Number of blocked contact for the date  # noqa: E501

        :return: The blocked of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this GetTransacSmsReportReports.

        Number of blocked contact for the date  # noqa: E501

        :param blocked: The blocked of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if blocked is None:
            raise ValueError("Invalid value for `blocked`, must not be `None`")  # noqa: E501

        self._blocked = blocked

    @property
    def unsubscribed(self):
        """Gets the unsubscribed of this GetTransacSmsReportReports.  # noqa: E501

        Number of unsubscription for the date  # noqa: E501

        :return: The unsubscribed of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """Sets the unsubscribed of this GetTransacSmsReportReports.

        Number of unsubscription for the date  # noqa: E501

        :param unsubscribed: The unsubscribed of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if unsubscribed is None:
            raise ValueError("Invalid value for `unsubscribed`, must not be `None`")  # noqa: E501

        self._unsubscribed = unsubscribed

    @property
    def replied(self):
        """Gets the replied of this GetTransacSmsReportReports.  # noqa: E501

        Number of answered SMS for the date  # noqa: E501

        :return: The replied of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._replied

    @replied.setter
    def replied(self, replied):
        """Sets the replied of this GetTransacSmsReportReports.

        Number of answered SMS for the date  # noqa: E501

        :param replied: The replied of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if replied is None:
            raise ValueError("Invalid value for `replied`, must not be `None`")  # noqa: E501

        self._replied = replied

    @property
    def accepted(self):
        """Gets the accepted of this GetTransacSmsReportReports.  # noqa: E501

        Number of accepted for the date  # noqa: E501

        :return: The accepted of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this GetTransacSmsReportReports.

        Number of accepted for the date  # noqa: E501

        :param accepted: The accepted of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if accepted is None:
            raise ValueError("Invalid value for `accepted`, must not be `None`")  # noqa: E501

        self._accepted = accepted

    @property
    def rejected(self):
        """Gets the rejected of this GetTransacSmsReportReports.  # noqa: E501

        Number of rejected for the date  # noqa: E501

        :return: The rejected of this GetTransacSmsReportReports.  # noqa: E501
        :rtype: int
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this GetTransacSmsReportReports.

        Number of rejected for the date  # noqa: E501

        :param rejected: The rejected of this GetTransacSmsReportReports.  # noqa: E501
        :type: int
        """
        if rejected is None:
            raise ValueError("Invalid value for `rejected`, must not be `None`")  # noqa: E501

        self._rejected = rejected

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
        if issubclass(GetTransacSmsReportReports, dict):
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
        if not isinstance(other, GetTransacSmsReportReports):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
