node {

    
    long BUILDNUM = System.currentTimeMillis()/ 1000

    
    stage('Pull Source Dev') {
        
        git pull: 'master', changelog: true, poll: false, url: 'git@github.com:aushetty/dbdm.trials.git'
       
        sh '''
                mkdir -p ${WORKSPACE}/${BUILDNUM}
                cd ${WORKSPACE}/${BUILDNUM} 
                ls -l       
                
        '''
        
    }


    stage ('Build') {
         sh '''
            cd ${WORKSPACE}/${BUILDNUM}

            cat Dockerfile

        '''

  }

  stage('Deploy'){

         sh """
            /usr/local/bin/kubectl config set-context --current --namepsace=ibm-dev
            /usr/local/bin/kubectl apply -f ${WORKSPACE}/deploysec.yaml
            """

  }
   

}