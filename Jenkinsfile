node('master')
{
	stage ('checkout')
	{
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
		input('Are you sure?')
		echo 'deploying'
	}
			
}

