from LsPrePost import execute_command
from typing import List, Union
from .ShapeM import Point


def create_shell_by_solid_face(element_id: int,
                               part_id: int) -> None:
    execute_command("elgenerate shelltype 2")
    execute_command("genselect target segment")
    execute_command("genselect allvis")
    execute_command(f"elgenerate shell solidface {part_id} {element_id}")
    execute_command("elgenerate accept")


def create_solid_cohesive(element_id: int,
                          part_id: int,
                          pre_cohesive_parts: List[int],
                          connect_parts: List[int]) -> None:
    pre_cohesive_parts = " ".join(map(str, pre_cohesive_parts))
    connect_parts = " ".join(map(str, connect_parts))
    execute_command(f"elgenerate solid cohesive precohesparts {pre_cohesive_parts}")
    execute_command(f"elgenerate solid cohesive connectparts {connect_parts}")
    execute_command(f"elgenerate solid cohesive create {element_id} {part_id}")


def create_solid_by_shell_spin(element_id: int,
                               part_id: int,
                               selected_part_id: int,
                               angle: Union[int, float],
                               segment: int,
                               position: Point,
                               direction: Point) -> None:
    execute_command("genselect target edge")
    execute_command("genselect target segment")
    execute_command("genselect target shell")
    execute_command(f"genselect shell add part {selected_part_id}/0")
    execute_command(f"elgenerate solid shellspin {part_id} "
                    f"{element_id} "
                    f"{angle} "
                    f"{segment} "
                    f"{position.x} {position.y} {position.z} "
                    f"{position.x+direction.x/40} {position.y+direction.y/40} {position.z+direction.z/40}")
    execute_command(f"elgenerate accept")
