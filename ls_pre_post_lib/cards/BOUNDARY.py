from dataclasses import dataclass, field
from typing import Union, List
from .card import ICard
#айкард - интерфейс который определяет методы чтоб крточка занеслась в к файл
#юнион лист - обознаает тип переменных
#фиелдэто занесение в список для того чтоб передать список в параметр датакласса
@dataclass #ячейки хранилища с параметрами
class PRESCRIBED_MOTION_SET(ICard):
    """

    NSID:=Nodal set ID, see *SET_NODE.
    -----------------------------------------------------------------
    DOF:=Applicable degrees-of-freedom:
    EQ.0: Not valid, please use any of the other available options,
    EQ.1: x-translational DOF
    EQ.2: y-translational DOF
    EQ.3: z-translational DOF
    EQ.4: translational motion only in direction given by the VID.
          Movement on plane normal to the vector is permitted
    EQ.-4: Same as 4, except translation on the plane normal to the
           vector is NOT permitted
    EQ.5: x-rotational DOF
    EQ.6: y-rotational DOF
    EQ.7: z-rotational DOF
    EQ.8: rotational motion about an axis which is passing through
          the center-of-gravity of the node, node set, or rigid body
          and is parallel to vector VID.  Rotation about the normal
          axes is permitted
    EQ.-8: rotational motion about an axis which is passing through
           the center-of-gravity of the node or node set and is
           parallel to vector VID.  Rotation about the normal axes is
           not permitted.  This option does not apply to rigid bodies
    EQ.9: y/z DOF for node rotating about the x-axis at location
          (OFFSET1,OFFSET2) in the yz-plane, point (y,z). Radial
          motion is NOT permitted
    EQ.-9: Same as 9, except radial motion is permitted
    EQ.10: z/x DOF for node rotating about the y-axis at location
           (OFFSET1,OFFSET2) in the zx-plane, point(z,x). Radial
           motion is NOT permitted
    EQ.-10:Same as  10, except radial motion is permitted,
    EQ.11: x/y DOF for node rotating about the z-axis at location
           (OFFSET1,OFFSET2) in the xy-plane, point (x,y). Radial
           motion is NOT permitted
    EQ.-11: Same as 11, except radial motion is permitted.
    EQ.12: Translational motion in direction given by the normals to
           the segments. Applicable to SET_SEGMENT option only
    -----------------------------------------------------------------
    VAD:=Velocity/Acceleration/Displacement flag:
    EQ.0: velocity(rigid bodies and nodes),
    EQ.1: acceleration(nodes only),
    EQ.2: displacement(rigid bodies and nodes).
    EQ.3: velocity versus displacement(rigid bodies),
    EQ.4: relative displacement(rigid bodies only)
    -----------------------------------------------------------------
    LCID:=Curve ID or function ID to describe motion value as a
          function of time; see *DEFINE_CURVE,
          *DEFINE_CURVE_FUNCTION, or *DEFINE_FUNCTION.  If LCID
          refers to *DEFINE_FUNCTION, the function has four
          arguments: time and x, y and z coordinates of the node or
          rigid body, such as f(t,x,y,z)=10.0Г—t+maxвЃЎ(x-100,0.). If
          VAD = 2, the function has one argument which is time, such
          as f(t)=10.0Г—t (see Remark 2). See BIRTH below
    -----------------------------------------------------------------
    SF:=Load curve scale factor (default=1.0).
    -----------------------------------------------------------------
    VID:=Vector ID for DOF values of 4 or 8, see *DEFINE_VECTOR.
    -----------------------------------------------------------------
    DEATH:=Time imposed motion/constraint is removed
           (default=1.0E+28).
    -----------------------------------------------------------------
    BIRTH:=Time imposed motion/constraint is activated (default=0.0).

    """
    name: str = "BOUNDARY_PRESCRIBED_MOTION_SET"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    NSID: int = ""
    DOF: [0, 1, 2, 3, 4, -4, 5, 6, 7, 8, -8, 9, -9, 10, -10, 11, -11, 12] = 0
    VAD: [0, 1, 2, 3, 4] = 0
    LCID: int = ""
    SF: Union[int, float] = 1.0
    VID: int = ""
    DEATH: Union[int, float] = 1.0e28
    BIRTH: Union[int, float] = 0.0


@dataclass
class SPC_SET(ICard):
    """

    NSID:=Nodal set ID, see also *SET_NODE.
    -----------------------------------------------------------------
    CID:=Coordinate system ID, see *DEFINE_COORDINATE_SYSTEM.
    -----------------------------------------------------------------
    DOFX:=EQ.0: no translational constraint in local x-direction,
    EQ.1: translational constraint in local x-direction.
    -----------------------------------------------------------------
    DOFY:=EQ.0: no translational constraint in local y-direction,
    EQ.1: translational constraint in local y-direction.
    -----------------------------------------------------------------
    DOFZ:=EQ.0: no translational constraint in local z-direction,
    EQ.1: translational constraint in local z-direction.
    -----------------------------------------------------------------
    DOFRX:=EQ.0: no rotational constraint about the local x-axis,
    EQ.1: rotational constraint about local x-axis.
    -----------------------------------------------------------------
    DOFRY:=EQ.0: no rotational constraint about the local y-axis,
    EQ.1: rotational constraint about local y-axis.
    -----------------------------------------------------------------
    DOFRZ:=EQ.0: no rotational constraint about the local z-axiis
    EQ.1: rotational constraint about local z-axis.

    """
    name: str = "BOUNDARY_SPC_SET"
    rows_lengths: List[int] = field(default_factory=lambda: [8])

    NSID: int = ""
    CID: int = ""
    DOFX: [0, 1] = 0
    DOFY: [0, 1] = 0
    DOFZ: [0, 1] = 0
    DOFRX: [0, 1] = 0
    DOFRY: [0, 1] = 0
    DOFRZ: [0, 1] = 0

