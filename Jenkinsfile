pipeline {
    agent any

    parameters {
        string(name: 'CRIPTO', defaultValue: 'bitcoin', description: 'Nombre de la criptomoneda (ej: bitcoin, ethereum)')
        string(name: 'MONEDA', defaultValue: 'usd', description: 'Moneda de referencia (ej: usd, eur, clp)')
        string(name: 'DIAS', defaultValue: '7', description: 'Cantidad de días para el gráfico (ej: 7, 30, 90)')
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

        stage('Ejecutar contenedor con entradas simuladas') {
            steps {
                powershell """
                    docker rm -f crypto_app_container 2>\$null
                    \\"${params.CRIPTO}\`n${params.MONEDA}\`n${params.DIAS}\\" | docker run --name crypto_app_container --rm -i crypto_app
                """
            }
        }
    }
}
