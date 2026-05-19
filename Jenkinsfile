pipeline {
    agent any

    parameters {
        choice(name: 'CRIPTO', choices: ['bitcoin', 'ethereum', 'dogecoin'], description: 'Selecciona la criptomoneda')
        choice(name: 'MONEDA', choices: ['usd', 'eur', 'clp'], description: 'Selecciona la moneda de referencia')
        choice(name: 'DIAS', choices: ['7', '30', '90'], description: 'Cantidad de días para el gráfico')
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

        stage('Ejecutar contenedor con parámetros seguros') {
            steps {
                powershell '''
                    # Como vienen de choice, no hay BOM ni \r
                    $cripto = "${env:CRIPTO}"
                    $moneda = "${env:MONEDA}"
                    $dias   = "${env:DIAS}"

                    Set-Content -Path respuestas.txt -Value $cripto
                    Add-Content -Path respuestas.txt -Value $moneda
                    Add-Content -Path respuestas.txt -Value $dias

                    docker rm -f crypto_app_container 2>$null
                    Get-Content respuestas.txt | docker run --name crypto_app_container --rm -i crypto_app
                '''
            }
        }
    }
}
