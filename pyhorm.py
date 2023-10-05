import numpy as np
from stl import mesh

# Definir los puntos y caras del hormiguero
points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                   [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
faces = np.array([[0, 1, 2], [0, 2, 3], [4, 5, 6], [4, 6, 7],
                  [0, 4, 5], [0, 5, 1], [2, 6, 7], [2, 7, 3],
                  [0, 3, 7], [0, 7, 4], [1, 5, 6], [1, 6, 2]])

# Definir las transformaciones y ubicaciones de los cubos
transformations = [
    {'scale': [1.5, 1.0, 1.0], 'translate': [0.0, 0.0, 0.0]},
    {'scale': [1.0, 1.5, 1.0], 'translate': [1.5, 0.0, 0.0]},
    {'scale': [1.0, 1.0, 1.5], 'translate': [0.0, 0.0, 1.0]}
]

# Crear el objeto de malla STL
hormiguero_mesh = mesh.Mesh(np.zeros(faces.shape[0] * len(transformations),
                                     dtype=mesh.Mesh.dtype))

# Generar los cubos para cada transformación
for i, transform in enumerate(transformations):
    cube = mesh.Mesh(np.zeros_like(hormiguero_mesh.data))
    for j, face in enumerate(faces):
        for k, vertex in enumerate(face):
            cube.vectors[j][k] = points[vertex]

    # Aplicar la transformación al cubo
    cube.data['vectors'] *= np.array(transform['scale'])
    cube.data['vectors'] += np.array(transform['translate'])

    # Agregar el cubo transformado a la malla del hormiguero
    hormiguero_mesh.vectors[i * len(faces):(i + 1) * len(faces)] = cube.vectors

# Guardar la malla en un archivo STL
hormiguero_mesh.save('hormiguero.stl')
