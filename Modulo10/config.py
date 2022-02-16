def main():
    try:
        configuration = open("D:\\Users\\Victor\\Escritorio\\Archivos Compartidos\\Cursos WIP\\LaunchX\\Jupyter Python\\Modulo10\\config.txt\\")
    except FileNotFoundError as err:
        print("No se pudo hallar el archivo", err)
    except IsADirectoryError:
        print("config.txt existe pero es un directorio")

if __name__ == '__main__':
    main()

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    if err.errno == 13:
        print("Found config.txt but couldn't read it")

