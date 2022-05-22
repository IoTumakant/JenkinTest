pipeline {
	agent any 
	stages { 
		stage('Build') {
			steps { echo 'Build is in progress....'
            }
        }
		stage('Test'){ 
			steps { echo 'Test is in progress...'
				script {
					#sh 'python TimeLog_file.py'
				}	
		}
        }
		stage('Deploy'){
			 steps { echo 'Deploy is in proress..'
            }
        }    
    }
}    
