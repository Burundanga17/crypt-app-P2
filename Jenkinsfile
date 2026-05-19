pipeline {
    agent any

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
                    
                    // 🔹 Aquí usamos echo para simular los 3 input()
                    // Primera línea: cripto
                    // Segunda línea: moneda
                    // Tercera línea: días
                    sh '(echo bitcoin && echo usd && echo 7) | docker run --name crypto_app_container --rm -i crypto_app'
                }
            }
        }
    }
}
