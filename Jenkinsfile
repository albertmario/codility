node('master')
{
	stage ('checkout')
	{
		notifystarted()
		checkout scm

	}
	stage ('SonarQube testing')
	{
		def scannerhome = tool 'SonarScanner';
		withSonarQubeEnv('SonarQube')
		{
			sh "${scannerhome}/bin/sonar-scanner"
		}
	}
	stage('deploy')
	{
		//mail (to:'albertmario19@gmail.com', subject:'Pipeline test', body:'ini lagi nunggu gan, uda kelar');
		input('Are you sure?')
	}
	
	def notifystarted()
	{
		emailext
		(
			subject: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", 
			body: """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
			<p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>""",
			recipientProviders: [[$class: 'DevelopersRecipientProvider']]
		)
	}	
}

