from dataclasses import dataclass
from ..geometry import IGeometry
from LsPrePost import execute_command
from typing import Union


__all__ = ['Point',
           'BoxSolid',
           'BoxShell',
           'FourNShell',
           'SphereSolid',
           'SphereShell',
           'CylinderSolid',
           'CylinderShell',
           'CircleShell']


@dataclass
class Point:
    """

    x:=value along x
    -----------------------------------------------------------------
    y:=value along y
    -----------------------------------------------------------------
    z:=value along z

    """
    x: Union[int, float] = 0
    y: Union[int, float] = 0
    z: Union[int, float] = 0


@dataclass
class Box:
    """

    P_min:=minimum point
    -----------------------------------------------------------------
    P_max:=maximum point
    -----------------------------------------------------------------
    Vx:=number of elements along x
    -----------------------------------------------------------------
    Vy:=number of elements along y
    -----------------------------------------------------------------
    Vz:=number of elements along z
    -----------------------------------------------------------------
    Gap:=gap distance, extending the values above
    -----------------------------------------------------------------
    TargetName:=target part name
    -----------------------------------------------------------------
    TargetPartID:=target part id
    -----------------------------------------------------------------
    StartElementID:=starting element id
    -----------------------------------------------------------------
    StartNodeID:=starting node id

    """
    P_min: Point = Point()
    P_max: Point = Point(x=100, y=100, z=100)

    Vx: int = 1
    Vy: int = 1
    Vz: int = 1
    Gap: int = 0

    TargetPartID: int = 0
    TargetName: str = "box"
    StartElementID: int = 0
    StartNodeID: int = 0


@dataclass
class Plane4Point:
    """

    P1:=first point
    -----------------------------------------------------------------
    P2:=second point
    -----------------------------------------------------------------
    P3:=third point
    -----------------------------------------------------------------
    P4:=fourth point
    -----------------------------------------------------------------
    NxNo:=number of elements along x
    -----------------------------------------------------------------
    NyNo:=number of elements along y

    """
    P1: Point = Point()
    P2: Point = Point()
    P3: Point = Point()
    P4: Point = Point()

    NxNo: int = 5
    NyNo: int = 5

    TargetPartID: int = 0
    TargetName: str = "plane4point"
    StartElementID: int = 0
    StartNodeID: int = 0


@dataclass
class Sphere:
    """

    """
    pass


@dataclass
class Cylinder:
    """

    """
    pass


@dataclass
class Circle:
    """

    """
    pass


class BoxSolid(Box, IGeometry):
    """
    meshed solid box based on teo points: P_min, P_max
    """
    def create(self) -> None:
        execute_command('cemptymodel')
        execute_command('genselect target node')
        execute_command('genselect clear')
        execute_command('meshing boxsolid create '
                        f'{self.P_min.x} {self.P_min.y} {self.P_min.z} '
                        f'{self.P_max.x} {self.P_max.y} {self.P_max.z} '
                        f'{self.Vx} {self.Vy} {self.Vz} {self.Gap}')
        execute_command('meshing boxsolid accept '
                        f'{self.TargetPartID} '
                        f'{self.StartElementID} '
                        f'{self.StartNodeID} '
                        f'{self.TargetName}')
        execute_command('ac')


class BoxShell(Box, IGeometry):
    """
    meshed shell box based on two points: P_min, P_max
    """
    def create(self) -> None:
        execute_command('cemptymodel')
        execute_command('genselect target node')
        execute_command('genselect clear')
        execute_command('meshing boxshell create '
                        f'{self.P_min.x} {self.P_min.y} {self.P_min.z} '
                        f'{self.P_max.x} {self.P_max.y} {self.P_max.z} '
                        f'{self.Vx} {self.Vy} {self.Vz} {self.Gap}')
        execute_command('meshing boxshell accept '
                        f'{self.TargetPartID} '
                        f'{self.StartElementID} '
                        f'{self.StartNodeID} '
                        f'{self.TargetName}')
        execute_command('ac')


class FourNShell(Plane4Point, IGeometry):
    """
    meshed quadrilateral plane based on four points: P1, P2, P3, P4
    """
    def create(self) -> None:
        execute_command('cemptymodel')
        execute_command('genselect target node')
        execute_command('genselect clear')
        execute_command('meshing 4pshell create '
                        f'{self.NxNo} {self.NyNo} '
                        f'{self.P1.x} {self.P1.y} {self.P1.z} '
                        f'{self.P2.x} {self.P2.y} {self.P2.z} ' 
                        f'{self.P3.x} {self.P3.y} {self.P3.z} '
                        f'{self.P4.x} {self.P4.y} {self.P4.z}')
        execute_command('meshing 4pshell accept '
                        f'{self.TargetPartID} '
                        f'{self.StartElementID} '
                        f'{self.StartNodeID} '
                        f'{self.TargetName}')
        execute_command('ac')


class SphereSolid(Sphere, IGeometry):
    """

    """
    def create(self) -> None:
        pass


class SphereShell(Sphere, IGeometry):
    """

    """
    def create(self) -> None:
        pass


class CylinderSolid(Sphere, IGeometry):
    """

    """
    def create(self) -> None:
        pass


class CylinderShell(Sphere, IGeometry):
    """

    """
    def create(self) -> None:
        pass


class CircleShell(Sphere, IGeometry):
    """

    """
    def create(self) -> None:
        pass
