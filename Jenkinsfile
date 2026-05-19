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

        stage('Ejecutar contenedor') {
            steps {
                script {
                    // Elimina contenedor previo si existe
                    sh 'docker rm -f crypto_app_container || echo "No existe contenedor previo"'
                    // Ejecuta en modo detached
                    sh 'docker run --name crypto_app_container -d crypto_app'
                }
            }
        }
    }
}
