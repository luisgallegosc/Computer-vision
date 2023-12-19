import cv2

# Reemplaza la ruta con la tuya
ruta_imagen_original = "C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\imagen.png"
ruta_elemento_estructurante = "C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\estructurante.png"

imagen_original = cv2.imread(ruta_imagen_original, cv2.IMREAD_GRAYSCALE)
elemento_estructurante = cv2.imread(ruta_elemento_estructurante, cv2.IMREAD_GRAYSCALE)  # Corregir nombre de variable

# Verificar si la carga de las imágenes fue exitosa
if imagen_original is None or elemento_estructurante is None:
    print("Error al cargar la imagen o el elemento estructurante.")
else:
    # Aplicar la operación de apertura utilizando el elemento estructurante
    imagen_apertura = cv2.morphologyEx(imagen_original, cv2.MORPH_OPEN, elemento_estructurante)

    # Mostrar las imágenes
    cv2.imshow("Imagen Original", imagen_original)
    cv2.imshow("Elemento Estructurante", elemento_estructurante)
    cv2.imshow("Imagen Después de Apertura", imagen_apertura)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

