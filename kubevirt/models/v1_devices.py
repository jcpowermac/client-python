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


class V1Devices(object):
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
        'channels': 'list[V1Channel]',
        'consoles': 'list[V1Console]',
        'disks': 'list[V1Disk]',
        'emulator': 'str',
        'graphics': 'list[V1Graphics]',
        'interfaces': 'list[V1Interface]',
        'memballoon': 'V1Ballooning',
        'serials': 'list[V1Serial]',
        'video': 'list[V1Video]',
        'watchdog': 'V1Watchdog'
    }

    attribute_map = {
        'channels': 'channels',
        'consoles': 'consoles',
        'disks': 'disks',
        'emulator': 'emulator',
        'graphics': 'graphics',
        'interfaces': 'interfaces',
        'memballoon': 'memballoon',
        'serials': 'serials',
        'video': 'video',
        'watchdog': 'watchdog'
    }

    def __init__(self, channels=None, consoles=None, disks=None, emulator=None, graphics=None, interfaces=None, memballoon=None, serials=None, video=None, watchdog=None):
        """
        V1Devices - a model defined in Swagger
        """

        self._channels = None
        self._consoles = None
        self._disks = None
        self._emulator = None
        self._graphics = None
        self._interfaces = None
        self._memballoon = None
        self._serials = None
        self._video = None
        self._watchdog = None

        if channels is not None:
          self.channels = channels
        if consoles is not None:
          self.consoles = consoles
        if disks is not None:
          self.disks = disks
        if emulator is not None:
          self.emulator = emulator
        if graphics is not None:
          self.graphics = graphics
        if interfaces is not None:
          self.interfaces = interfaces
        if memballoon is not None:
          self.memballoon = memballoon
        if serials is not None:
          self.serials = serials
        if video is not None:
          self.video = video
        if watchdog is not None:
          self.watchdog = watchdog

    @property
    def channels(self):
        """
        Gets the channels of this V1Devices.

        :return: The channels of this V1Devices.
        :rtype: list[V1Channel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this V1Devices.

        :param channels: The channels of this V1Devices.
        :type: list[V1Channel]
        """

        self._channels = channels

    @property
    def consoles(self):
        """
        Gets the consoles of this V1Devices.

        :return: The consoles of this V1Devices.
        :rtype: list[V1Console]
        """
        return self._consoles

    @consoles.setter
    def consoles(self, consoles):
        """
        Sets the consoles of this V1Devices.

        :param consoles: The consoles of this V1Devices.
        :type: list[V1Console]
        """

        self._consoles = consoles

    @property
    def disks(self):
        """
        Gets the disks of this V1Devices.

        :return: The disks of this V1Devices.
        :rtype: list[V1Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this V1Devices.

        :param disks: The disks of this V1Devices.
        :type: list[V1Disk]
        """

        self._disks = disks

    @property
    def emulator(self):
        """
        Gets the emulator of this V1Devices.

        :return: The emulator of this V1Devices.
        :rtype: str
        """
        return self._emulator

    @emulator.setter
    def emulator(self, emulator):
        """
        Sets the emulator of this V1Devices.

        :param emulator: The emulator of this V1Devices.
        :type: str
        """

        self._emulator = emulator

    @property
    def graphics(self):
        """
        Gets the graphics of this V1Devices.

        :return: The graphics of this V1Devices.
        :rtype: list[V1Graphics]
        """
        return self._graphics

    @graphics.setter
    def graphics(self, graphics):
        """
        Sets the graphics of this V1Devices.

        :param graphics: The graphics of this V1Devices.
        :type: list[V1Graphics]
        """

        self._graphics = graphics

    @property
    def interfaces(self):
        """
        Gets the interfaces of this V1Devices.

        :return: The interfaces of this V1Devices.
        :rtype: list[V1Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this V1Devices.

        :param interfaces: The interfaces of this V1Devices.
        :type: list[V1Interface]
        """

        self._interfaces = interfaces

    @property
    def memballoon(self):
        """
        Gets the memballoon of this V1Devices.

        :return: The memballoon of this V1Devices.
        :rtype: V1Ballooning
        """
        return self._memballoon

    @memballoon.setter
    def memballoon(self, memballoon):
        """
        Sets the memballoon of this V1Devices.

        :param memballoon: The memballoon of this V1Devices.
        :type: V1Ballooning
        """

        self._memballoon = memballoon

    @property
    def serials(self):
        """
        Gets the serials of this V1Devices.

        :return: The serials of this V1Devices.
        :rtype: list[V1Serial]
        """
        return self._serials

    @serials.setter
    def serials(self, serials):
        """
        Sets the serials of this V1Devices.

        :param serials: The serials of this V1Devices.
        :type: list[V1Serial]
        """

        self._serials = serials

    @property
    def video(self):
        """
        Gets the video of this V1Devices.

        :return: The video of this V1Devices.
        :rtype: list[V1Video]
        """
        return self._video

    @video.setter
    def video(self, video):
        """
        Sets the video of this V1Devices.

        :param video: The video of this V1Devices.
        :type: list[V1Video]
        """

        self._video = video

    @property
    def watchdog(self):
        """
        Gets the watchdog of this V1Devices.

        :return: The watchdog of this V1Devices.
        :rtype: V1Watchdog
        """
        return self._watchdog

    @watchdog.setter
    def watchdog(self, watchdog):
        """
        Sets the watchdog of this V1Devices.

        :param watchdog: The watchdog of this V1Devices.
        :type: V1Watchdog
        """

        self._watchdog = watchdog

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
        if not isinstance(other, V1Devices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other