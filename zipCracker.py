import pyzipper
import argparse


def extraerArchivo(fileZip, password):
    """
    Extrae archivos de un archivo comprimido utilizando una contraseña proporcionada.

    :param fileZip: Un objeto de archivo zip.
    :type fileZip: zipfile.ZipFile
    :param password: La contraseña para extraer los archivos del archivo zip.
    :type password: bytes

    :return: Verdadero si la extracción fue exitosa, Falso de lo contrario.
    :rtype: bool
    """

    try:
        fileZip.extractall(pwd=password)
        print("Contraseña encontrada => " + password.decode("utf-8"))
        return True
    except:
        return False


def main():
    """
    Analiza los argumentos de línea de comandos para extraer el contenido de un archivo zip utilizando un diccionario.

    Args:
        None

    Returns:
        None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest="file", help="archivo a extraer")
    parser.add_argument('-d', '--dict', dest="dict", help="diccionario a usar")
    args = parser.parse_args()

    if args.file is None:
        print("Ingrese los parámetros necesarios")
        exit(0)
    elif args.dict is None:
        archivoZip = args.file
        diccionario = "diccionario.txt"
    else:
        archivoZip = args.file
        diccionario = args.dict

    fileZip = pyzipper.AESZipFile(archivoZip)

    with open(diccionario, "rb") as f:
        for line in f.readlines():
            password = line.strip()
            if extraerArchivo(fileZip, password):
                exit(0)

        print("No se encontró la contraseña")


if __name__ == "__main__":
    main()
