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
		mail (to:'albertmario19@gmail.com', subject:'Pipeline test', body:'ini lagi nunggu gan, uda kelar');
		input('Are you sure?')
	}
			
}

