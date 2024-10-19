from typing import Final, overload, type_check_only

from typing_extensions import Literal, TypeAlias

AF_12844: Final[int]
AF_APPLETALK: Final[int]
AF_ASH: Final[int]
AF_ATM: Final[int]
AF_ATMPVC: Final[int]
AF_ATMSVC: Final[int]
AF_AX25: Final[int]
AF_BAN: Final[int]
AF_BLUETOOTH: Final[int]
AF_BRIDGE: Final[int]
AF_DATAKIT: Final[int]
AF_DECnet: Final[int]
AF_CCITT: Final[int]
AF_CHAOS: Final[int]
AF_CLUSTER: Final[int]
AF_CNT: Final[int]
AF_COIP: Final[int]
AF_DLI: Final[int]
AF_ECONET: Final[int]
AF_ECMA: Final[int]
AF_FILE: Final[int]
AF_FIREFOX: Final[int]
AF_HYLINK: Final[int]
AF_IMPLINK: Final[int]
AF_INET: Final[int]
AF_INET6: Final[int]
AF_IPX: Final[int]
AF_IRDA: Final[int]
AF_ISDN: Final[int]
AF_ISO: Final[int]
AF_KEY: Final[int]
AF_LAT: Final[int]
AF_LINK: Final[int]
AF_NATM: Final[int]
AF_NETBEUI: Final[int]
AF_NETBIOS: Final[int]
AF_NETDES: Final[int]
AF_NETGRAPH: Final[int]
AF_NETLINK: Final[int]
AF_NETROM: Final[int]
AF_NDRV: Final[int]
AF_NS: Final[int]
AF_PACKET: Final[int]
AF_PPP: Final[int]
AF_PPPOX: Final[int]
AF_PUP: Final[int]
AF_ROSE: Final[int]
AF_ROUTE: Final[int]
AF_SECURITY: Final[int]
AF_SIP: Final[int]
AF_SNA: Final[int]
AF_SYSTEM: Final[int]
AF_UNIX: Final[int]
AF_UNKNOWN1: Final[int]
AF_UNSPEC: Final[int]
AF_VOICEVIEW: Final[int]
AF_WANPIPE: Final[int]
AF_X25: Final[int]
IN6_IFF_AUTOCONF: Final[int]
IN6_IFF_TEMPORARY: Final[int]
IN6_IFF_DYNAMIC: Final[int]
IN6_IFF_OPTIMISTIC: Final[int]
IN6_IFF_SECURED: Final[int]

address_families: Final[dict[int, str]]
version: Final[str]

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
