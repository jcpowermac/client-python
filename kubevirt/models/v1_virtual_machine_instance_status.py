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


class V1VirtualMachineInstanceStatus(object):
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
        'conditions': 'list[V1VirtualMachineInstanceCondition]',
        'interfaces': 'list[V1VirtualMachineInstanceNetworkInterface]',
        'node_name': 'str',
        'phase': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'interfaces': 'interfaces',
        'node_name': 'nodeName',
        'phase': 'phase'
    }

    def __init__(self, conditions=None, interfaces=None, node_name=None, phase=None):
        """
        V1VirtualMachineInstanceStatus - a model defined in Swagger
        """

        self._conditions = None
        self._interfaces = None
        self._node_name = None
        self._phase = None

        if conditions is not None:
          self.conditions = conditions
        if interfaces is not None:
          self.interfaces = interfaces
        if node_name is not None:
          self.node_name = node_name
        if phase is not None:
          self.phase = phase

    @property
    def conditions(self):
        """
        Gets the conditions of this V1VirtualMachineInstanceStatus.
        Conditions are specific points in VirtualMachineInstance's pod runtime.

        :return: The conditions of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VirtualMachineInstanceCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1VirtualMachineInstanceStatus.
        Conditions are specific points in VirtualMachineInstance's pod runtime.

        :param conditions: The conditions of this V1VirtualMachineInstanceStatus.
        :type: list[V1VirtualMachineInstanceCondition]
        """

        self._conditions = conditions

    @property
    def interfaces(self):
        """
        Gets the interfaces of this V1VirtualMachineInstanceStatus.
        Interfaces represent the details of available network interfaces.

        :return: The interfaces of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VirtualMachineInstanceNetworkInterface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this V1VirtualMachineInstanceStatus.
        Interfaces represent the details of available network interfaces.

        :param interfaces: The interfaces of this V1VirtualMachineInstanceStatus.
        :type: list[V1VirtualMachineInstanceNetworkInterface]
        """

        self._interfaces = interfaces

    @property
    def node_name(self):
        """
        Gets the node_name of this V1VirtualMachineInstanceStatus.
        NodeName is the name where the VirtualMachineInstance is currently running.

        :return: The node_name of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1VirtualMachineInstanceStatus.
        NodeName is the name where the VirtualMachineInstance is currently running.

        :param node_name: The node_name of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._node_name = node_name

    @property
    def phase(self):
        """
        Gets the phase of this V1VirtualMachineInstanceStatus.
        Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it.

        :return: The phase of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1VirtualMachineInstanceStatus.
        Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it.

        :param phase: The phase of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._phase = phase

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
        if not isinstance(other, V1VirtualMachineInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
