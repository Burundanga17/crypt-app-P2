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
                script {
                    sh 'docker build -t crypto_app .'
                }
            }
        }

        stage('Ejecutar contenedor con entradas simuladas') {
            steps {
                script {
                    // Elimina contenedor previo si existe
                    sh 'docker rm -f crypto_app_container || echo "No existe contenedor previo"'
                    
                    // 🔹 Usamos PowerShell-style newlines para simular input()
                    sh "\"${params.CRIPTO}`n${params.MONEDA}`n${params.DIAS}\" | docker run --name crypto_app_container --rm -i crypto_app"
                }
            }
        }
    }
}

