pipeline {
    agent any

    environment {
        CRIPTO = "bitcoin"
        MONEDA = "usd"
        DIAS   = "10"
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

        stage('Ejecutar contenedor y mostrar salida') {
            steps {
                script {
                    // Elimina contenedor previo si existe
                    sh 'docker rm -f crypto_app_container || echo "No existe contenedor previo"'
                    // Ejecuta en primer plano con variables de entorno
                    sh 'docker run --name crypto_app_container --rm -e CRIPTO=$CRIPTO -e MONEDA=$MONEDA -e DIAS=$DIAS crypto_app'
                }
            }
        }
    }
}

