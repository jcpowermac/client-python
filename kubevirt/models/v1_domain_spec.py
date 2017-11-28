# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DomainSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'clock': 'V1Clock',
        'devices': 'V1Devices',
        'memory': 'V1Memory',
        'os': 'V1OS',
        'sys_info': 'V1SysInfo',
        'type': 'str'
    }

    attribute_map = {
        'clock': 'clock',
        'devices': 'devices',
        'memory': 'memory',
        'os': 'os',
        'sys_info': 'sysInfo',
        'type': 'type'
    }

    def __init__(self, clock=None, devices=None, memory=None, os=None, sys_info=None, type=None):
        """
        V1DomainSpec - a model defined in Swagger
        """

        self._clock = None
        self._devices = None
        self._memory = None
        self._os = None
        self._sys_info = None
        self._type = None

        if clock is not None:
          self.clock = clock
        self.devices = devices
        self.memory = memory
        self.os = os
        if sys_info is not None:
          self.sys_info = sys_info
        self.type = type

    @property
    def clock(self):
        """
        Gets the clock of this V1DomainSpec.

        :return: The clock of this V1DomainSpec.
        :rtype: V1Clock
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """
        Sets the clock of this V1DomainSpec.

        :param clock: The clock of this V1DomainSpec.
        :type: V1Clock
        """

        self._clock = clock

    @property
    def devices(self):
        """
        Gets the devices of this V1DomainSpec.

        :return: The devices of this V1DomainSpec.
        :rtype: V1Devices
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this V1DomainSpec.

        :param devices: The devices of this V1DomainSpec.
        :type: V1Devices
        """
        if devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")

        self._devices = devices

    @property
    def memory(self):
        """
        Gets the memory of this V1DomainSpec.

        :return: The memory of this V1DomainSpec.
        :rtype: V1Memory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this V1DomainSpec.

        :param memory: The memory of this V1DomainSpec.
        :type: V1Memory
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")

        self._memory = memory

    @property
    def os(self):
        """
        Gets the os of this V1DomainSpec.

        :return: The os of this V1DomainSpec.
        :rtype: V1OS
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this V1DomainSpec.

        :param os: The os of this V1DomainSpec.
        :type: V1OS
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")

        self._os = os

    @property
    def sys_info(self):
        """
        Gets the sys_info of this V1DomainSpec.

        :return: The sys_info of this V1DomainSpec.
        :rtype: V1SysInfo
        """
        return self._sys_info

    @sys_info.setter
    def sys_info(self, sys_info):
        """
        Sets the sys_info of this V1DomainSpec.

        :param sys_info: The sys_info of this V1DomainSpec.
        :type: V1SysInfo
        """

        self._sys_info = sys_info

    @property
    def type(self):
        """
        Gets the type of this V1DomainSpec.

        :return: The type of this V1DomainSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1DomainSpec.

        :param type: The type of this V1DomainSpec.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1DomainSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other