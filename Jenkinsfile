node('master')
{
	stage 'checkout'
	{
		checkout scm
	}
	stage 'test'
	{
		def scannerhome = tool 'SonarScanner';
		withSonarQubeEnv('SonarQube')
		{
			sh "${scannerhome}/bin/sonar-scanner"
		}
	}
			
}

