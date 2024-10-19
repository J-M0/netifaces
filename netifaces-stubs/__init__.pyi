from typing import overload, type_check_only

from typing_extensions import Literal, TypeAlias

AF_12844: int
AF_APPLETALK: int
AF_ASH: int
AF_ATM: int
AF_ATMPVC: int
AF_ATMSVC: int
AF_AX25: int
AF_BAN: int
AF_BLUETOOTH: int
AF_BRIDGE: int
AF_DATAKIT: int
AF_DECnet: int
AF_CCITT: int
AF_CHAOS: int
AF_CLUSTER: int
AF_CNT: int
AF_COIP: int
AF_DLI: int
AF_ECONET: int
AF_ECMA: int
AF_FILE: int
AF_FIREFOX: int
AF_HYLINK: int
AF_IMPLINK: int
AF_INET: int
AF_INET6: int
AF_IPX: int
AF_IRDA: int
AF_ISDN: int
AF_ISO: int
AF_KEY: int
AF_LAT: int
AF_LINK: int
AF_NATM: int
AF_NETBEUI: int
AF_NETBIOS: int
AF_NETDES: int
AF_NETGRAPH: int
AF_NETLINK: int
AF_NETROM: int
AF_NDRV: int
AF_NS: int
AF_PACKET: int
AF_PPP: int
AF_PPPOX: int
AF_PUP: int
AF_ROSE: int
AF_ROUTE: int
AF_SECURITY: int
AF_SIP: int
AF_SNA: int
AF_SYSTEM: int
AF_UNIX: int
AF_UNKNOWN1: int
AF_UNSPEC: int
AF_VOICEVIEW: int
AF_WANPIPE: int
AF_X25: int
IN6_IFF_AUTOCONF: int
IN6_IFF_TEMPORARY: int
IN6_IFF_DYNAMIC: int
IN6_IFF_OPTIMISTIC: int
IN6_IFF_SECURED: int

address_families: dict[int, str]
version: str

# In reality, gateways() returns a normal `dict`. However, the
# current type system cannot accurately express a `dict` that has
# one literal string key that maps to one type and `int` keys that
# map to another. Without these aliases and subclass, the closest we
# could get would be this monstrosity:
#
# dict[int | Literal["default"], list[tuple[str, str, bool]] | dict[int, tuple[str, str]]]

_Gateway: TypeAlias = tuple[str, str, bool]
_DefaultGateway: TypeAlias = tuple[str, str]

_KT: TypeAlias = int | Literal["default"]
_VT: TypeAlias = list[_Gateway] | dict[int, _DefaultGateway]

@type_check_only
class _Gateways(dict[_KT, _VT]):
    @overload
    def __getitem__(self, key: Literal["default"], /) -> dict[int, _DefaultGateway]: ...
    @overload
    def __getitem__(self, key: int, /) -> list[_Gateway]: ...
    # We need this last overload or else everyone complains
    # about the signature being incompatible with `Mapping`
    @overload
    def __getitem__(self, key: _KT, /) -> _VT: ...

def gateways() -> _Gateways: ...
def ifaddresses(ifname: str, /) -> dict[int, list[dict[str, str]]]: ...
def interfaces() -> list[str]: ...
