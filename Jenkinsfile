pipeline {
    agent any

    stages {
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
                    \\"bitcoin`nusd`n7\\" | docker run --name crypto_app_container --rm -i crypto_app
                """
            }
        }
    }
}
