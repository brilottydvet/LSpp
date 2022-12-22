from dataclasses import dataclass, field
from typing import List, Union
from .card import ICard


@dataclass
class NodeLine:
    """

    NID1:=First node ID of the set.
    -----------------------------------------------------------------
    NID2:=Second node ID of the set.
    -----------------------------------------------------------------
    NID3:=Third node ID of the set.
    -----------------------------------------------------------------
    NID4:=Fourth node ID of the set.
    -----------------------------------------------------------------
    NID5:=Fifth node ID of the set.
    -----------------------------------------------------------------
    NID6:=Sixth node ID of the set.
    -----------------------------------------------------------------
    NID7:=Seventh node ID of the set.
    -----------------------------------------------------------------
    NID8:=Eighth node ID of the set.

    """
    NID1: int = ""
    NID2: int = ""
    NID3: int = ""
    NID4: int = ""
    NID5: int = ""
    NID6: int = ""
    NID7: int = ""
    NID8: int = ""


@dataclass
class PartLine:
    """
    PID1:=First part ID of the set.
    -----------------------------------------------------------------
    PID2:=Second part ID of the set.
    -----------------------------------------------------------------
    PID3:=Third part ID of the set.
    -----------------------------------------------------------------
    PID4:=Fourth part ID of the set.
    -----------------------------------------------------------------
    PID5:=Fifth part ID of the set.
    -----------------------------------------------------------------
    PID6:=Sixth part ID of the set.
    -----------------------------------------------------------------
    PID7:=Seventh part ID of the set.
    -----------------------------------------------------------------
    PID8:=Eighth part ID of the set.
    """
    PID1: int = ''
    PID2: int = ''
    PID3: int = ''
    PID4: int = ''
    PID5: int = ''
    PID6: int = ''
    PID7: int = ''
    PID8: int = ''


@dataclass
class SolidLine:
    """
    K1:=First solid element ID of the set.
    -----------------------------------------------------------------
    K2:=Second solid element ID of the set.
    -----------------------------------------------------------------
    K3:=Third solid element ID of the set.
    -----------------------------------------------------------------
    K4:=Fourth solid element ID of the set.
    -----------------------------------------------------------------
    K5:=Fifth solid element ID of the set.
    -----------------------------------------------------------------
    K6:=Sixth solid element ID of the set.
    -----------------------------------------------------------------
    K7:=Seventh solid element ID of the set.
    -----------------------------------------------------------------
    K8:=Eighth solid element ID of the set.
    """
    K1: int = ''
    K2: int = ''
    K3: int = ''
    K4: int = ''
    K5: int = ''
    K6: int = ''
    K7: int = ''
    K8: int = ''


@dataclass
class NODE_LIST(ICard):
    """

    SID:=Node set ID. All node sets should have a unique set ID.
    -----------------------------------------------------------------
    DA1:=First nodal attribute default value is 0.0.
    -----------------------------------------------------------------
    DA2:=Second nodal attribute default value is 0.0.
    -----------------------------------------------------------------
    DA3:=Third nodal attribute default value is 0.0.
    -----------------------------------------------------------------
    DA4:=Fourth nodal attribute default value is 0.0.
    -----------------------------------------------------------------
    SOLVER:=EQ.MECH: mechanics.
    EQ.CESE: CE/SE compressible fluid flow solver.
    EQ.ICFD: Incompressible fluid flow solver.
    -----------------------------------------------------------------
    ITS:=Specify coupling type across different scales in two-scale
         co-simulation. This flag should only be included for node
         sets that provide coupling information in the input file
         referred to by *INCLUDE_COSIM;
    EQ.1: Tied contact coupling
    EQ.2: Solid - in - shell immersed coupling

    """
    name: str = "SET_NODE_LIST"
    rows_lengths: List[int] = field(default_factory=lambda: [7])

    SID: int = 0
    DA1: Union[int, float] = 0.0
    DA2: Union[int, float] = 0.0
    DA3: Union[int, float] = 0.0
    DA4: Union[int, float] = 0.0
    SOLVER: str = 'MECH'
    ITS: [1, 2] = 1

    node_lines: List[dict] = field(default_factory=list)


@dataclass
class PART_LIST(ICard):
    """
    SID:=Part set ID. All part sets should have a unique set ID.
    -----------------------------------------------------------------
    DA1:=First attribute default value is 0.0.
    -----------------------------------------------------------------
    DA2:=Second attribute default value is 0.0.
    -----------------------------------------------------------------
    DA3:=Third attribute default value is 0.0.
    -----------------------------------------------------------------
    DA4:=Fourth attribute default value is 0.0.
    -----------------------------------------------------------------
    SOLVER:=EQ.MECH: mechanics.
    EQ.CESE: CE/SE compressible fluid flow solver.
    EQ.ICFD: Incompressible fluid flow solver.
    """
    name: str = "SET_PART_LIST"
    rows_lengths: List[int] = field(default_factory=lambda: [6])

    SID: int = 0
    DA1: Union[int, float] = 0.0
    DA2: Union[int, float] = 0.0
    DA3: Union[int, float] = 0.0
    DA4: Union[int, float] = 0.0
    SOLVER: str = 'MECH'

    part_lines: List[dict] = field(default_factory=list)


@dataclass
class SOLID(ICard):
    """

    SID:=Solid element set ID. All shell sets should have a unique
         set ID.
    -----------------------------------------------------------------
    SOLVER:=EQ.MECH: mechanics.
            EQ.CESE: CE/SE compressible fluid flow solver.
            EQ.ICFD: Incompressible fluid flow solver.

    """
    name: str = "SET_SOLID"
    rows_lengths: List[int] = field(default_factory=lambda: [2])

    SID: int = 0
    SOLVER: str = 'MECH'

    solid_lines: List[dict] = field(default_factory=list)
