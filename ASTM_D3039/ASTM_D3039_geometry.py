from LsPrePost import execute_command
from ls_pre_post_lib.geometry.Mesh.ShapeM import Point, FourNShell, BoxSolid
import json
import os


def main() -> None:
    with open(r'D:\Documents\CML\CML_LS-Dyna_scripts\ASTM_D3039_data.json') as file:
        model_data = json.load(file)
    # путь сохранения
    keyfile_path = model_data['keyfile_path']
    # название файла
    keyfile_name = model_data['keyfile_name']
    # постановка 3д или 2д
    problem_statement = model_data['problem_statement']
    L = model_data['L']
    b = model_data['b']

    lx = model_data['lx']
    ly = model_data['ly']
    lz = model_data['lz']

    if problem_statement == 0:
        BoxSolid(P_min=Point(),
                 P_max=Point(x=L, y=b),
                 Vx=lx,
                 Vy=ly,
                 Vz=lz,
                 TargetName="box_solid").create()
    elif problem_statement == 1:
        FourNShell(P1=Point(),
                   P2=Point(x=L),
                   P3=Point(x=L, y=b),
                   P4=Point(y=b),
                   NxNo=lx,
                   NyNo=ly,
                   TargetName="4p_shell").create()
    #сохр к файла
    execute_command(f'save keyword {os.sep.join([keyfile_path, keyfile_name])}')


if __name__ == "__main__":
    main()
