from file_eraser import FileEreaser
from file_mover import FileMover
from file_copier import FileCopier

print('[1] - File Eraser;'
      '\n[2] - File Mover;'
      '\n[3] - File Copier; ')

option = int(input('Option: '))

if option == 1:
    FileEreaser.start()

elif option == 2:
    FileMover.start()

elif option == 3:
    FileCopier.start()
