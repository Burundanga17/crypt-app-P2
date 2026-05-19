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

        stage('Ejecutar contenedor con archivo de respuestas') {
            steps {
                powershell '''
                    $cripto = "${env:CRIPTO}".Trim()
                    $moneda = "${env:MONEDA}".Trim()
                    $dias   = "${env:DIAS}".Trim()

                    # Crear archivo limpio con los parámetros
                    Set-Content -Path respuestas.txt -Value $cripto
                    Add-Content -Path respuestas.txt -Value $moneda
                    Add-Content -Path respuestas.txt -Value $dias

                    docker rm -f crypto_app_container 2>$null
                    docker run --name crypto_app_container --rm -i crypto_app < respuestas.txt
                '''
            }
        }
    }
}
