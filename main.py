from file_eraser import FileEreaser
from file_mover import FileMover
from file_copier import FileCopier
from file_creator import FileCreator

print('[1] - File Eraser;'
      '\n[2] - File Mover;'
      '\n[3] - File Copier; '
      '\n[4] - File Creator;')

option = int(input('Option: '))

if option == 1:
    FileEreaser.start()

elif option == 2:
    FileMover.start()

elif option == 3:
    FileCopier.start()

elif option == 4:
    FileCreator.start()
