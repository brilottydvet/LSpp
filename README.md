# LSpp

Автоматизированное построение k-файла стандарта ASTM D 3039 для Ls-Dyna

## Geometry
L - длина образца
b - ширина образца
problem_statement - [0, 1] постановка задачи (какой конструктор использовать) solid или shell
laminate_statement - [0, 1] вид укладки sublaminate или unidirectional_laminate

### Sublaminate
n - кол-во пар слоев
symmetry [0, 1] симметричнрсть уклалки относительно срединной линии
angle - угол укладки
t - толщина монослоя

## Unidirectional_laminate
n - кол-во слоев
angle - угол укладки
t - толщина монослоя

## Mesh
lx - кол-во эл. по длине
ly - кол-во эл. по ширине
lz - кол-во эл. по высоте

## Boundary
A - ширина зажимов
displ - смещение

## Control
termination_time - время моделирования
step - шаг по времени
