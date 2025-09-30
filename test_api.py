import requests
import numpy as np

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    print("Probando endpoint inicial /")
    r = requests.get(BASE_URL + "/")
    assert r.status_code == 200
    data = r.json()
    print("Respuesta:", data)
    print("OK")

def test_predict(casos: dict):
    print("Probando endpoint predicción...")

    answer = {}
    for label, features in casos.items():
        print(f"Probando {label}...")
        try:
            r = requests.post(
                BASE_URL + "/predict",
                json={"features": features}
            )
            if r.status_code == 200:
                data = r.json()
                # print("Respuesta:", data)
                print(f"{label}: prediction={data['prediction']}")
                answer[label] = data['prediction']
                print(f"Prueba de predicción completada correctamente para {label}!\n")
            elif r.status_code == 400:
                print(f"{label}: Error 400 - Solicitud mal formada. Features={features}")
                try:
                    error_body = r.json()
                    print("Detalle del error:", error_body, '\n')
                except ValueError:
                    print("No se pudo decodificar el cuerpo del error como JSON.")
                answer[label] = "Error 400"
            else:
                print(f"{label}: Error inesperado {r.status_code}. Features={features}")
                try:
                    error_body = r.json()
                    print("Detalle del error:", error_body, '\n')
                except ValueError:
                    print("No se pudo decodificar el cuerpo del error como JSON.\n")
                answer[label] = f"Error {r.status_code}"
        except requests.exceptions.RequestException as e:
            print(f"{label}: Fallo en la solicitud - {e} \n")
            answer[label] = "Fallo de conexión"
    return answer


if __name__ == "__main__":
    try:
        test_health()
        print("Prueba de estado completada correctamente!")
    except Exception as e:
        print("Error durante la prueba de estado:", e)
    # Casos de prueba con diferentes características
    test_cases = []
    rng = np.random.default_rng(42)
    for i in range(3):
        vector = []
        for j in range(30):
            vector.append(rng.random())
        test_cases.append({f"Caso_{i+1}": vector})

    test_cases.append(
        {
            "Caso_4": [4, 90, 80, 120, 26.2, 0.663, 42],  # Prueba error (7 características en vez de 30)
        }
    )
    test_cases.append(
        {
            "Caso_5": [4, 90, 80, 40, 'verde', 26.2, 0.663, 42]  # Prueba error (dato no numérico)
        },
    )
    for case in test_cases:
        test_predict(case)
