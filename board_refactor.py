from typing import List
from dataclasses import dataclass, field


@dataclass
class Board:
    board: list
    blanks: list = field(init=False)

    def __post_init__(self) -> None:
        self.blanks = [idx for idx, val in enumerate(self.board) if val == 0]

    @property
    def validation_sets(self) -> List[list]:
        ...

    @property
    def is_valid(self) -> bool:
        ...

    @property
    def has_violations(self) -> bool:
        ...

    @property
    def has_blanks(self) -> bool:
        for blank in self.blanks:
            if self.board[blank] == 0:
                return True
        return False

    def _draw_board(self) -> str:
        ...

    def show(self) -> None:
        print(self._draw_board())

    def __repr__(self) -> str:
        return self._draw_board()


# TESTING ----------------------------------------------------------

indicies = list(range(0, 81))
col = 1
row = 1
div_section = ' ' + ''.join(['-' for i in range(14)])
div = div_section + div_section + div_section

print(f'\n{div}')

for i in indicies:
    if col == 1:
        print('| ', end='')

    print(f'({i:02d})', end='')

    if col == 9:
        print(' |')
        col = 0
        row += 1

        if row in [4, 7]:
            print(div)

    elif col in [3, 6]:
        print(' | ', end='')

    col += 1

print(f'{div}\n')

"""
                       9
        3              3              3
 -------------- -------------- --------------
| (00)(01)(02) | (03)(04)(05) | (06)(07)(08) |
| (09)(10)(11) | (12)(13)(14) | (15)(16)(17) | 18
| (18)(19)(20) | (21)(22)(23) | (24)(25)(26) |
 -------------- -------------- --------------     27
| (27)(28)(29) | (30)(31)(32) | (33)(34)(35) |
| (36)(37)(38) | (39)(40)(41) | (42)(43)(44) | 18
| (45)(46)(47) | (48)(49)(50) | (51)(52)(53) |
 -------------- -------------- --------------     27 
| (54)(55)(56) | (57)(58)(59) | (60)(61)(62) |
| (63)(64)(65) | (66)(67)(68) | (69)(70)(71) | 18
| (72)(73)(74) | (75)(76)(77) | (78)(79)(80) |
 -------------- -------------- --------------

               3
 --------------
| (00)(01)(02) |
| (09)(10)(11) |
| (18)(19)(20) |
 --------------  18


"""
block = 3
side = block * block

for b in range(3):
    print(b+block)
