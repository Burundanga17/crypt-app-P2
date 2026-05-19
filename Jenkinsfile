pipeline {
    agent any

    parameters {
        string(name: 'CRIPTO', defaultValue: 'bitcoin', description: 'Nombre de la criptomoneda')
        string(name: 'MONEDA', defaultValue: 'usd', description: 'Moneda de referencia')
        string(name: 'DIAS', defaultValue: '7', description: 'Cantidad de días para el gráfico')
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/Burundanga17/crypt-app-P2.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                powershell '''
                    docker build -t crypto_app .
                '''
            }
        }

        stage('Ejecutar contenedor con parámetros limpios') {
            steps {
                powershell '''
                    # Normalizar parámetros: quitar espacios, saltos de línea y BOM
                    $cripto = "${env:CRIPTO}".Trim() -replace '[^a-zA-Z0-9-]', ''
                    $moneda = "${env:MONEDA}".Trim() -replace '[^a-zA-Z0-9-]', ''
                    $dias   = "${env:DIAS}".Trim() -replace '[^0-9]', ''

                    docker rm -f crypto_app_container 2>$null
                    "$cripto`n$moneda`n$dias" | docker run --name crypto_app_container --rm -i crypto_app
                '''
            }
        }
    }
}
