node {

    
    long BUILDNUM = System.currentTimeMillis()/ 1000

    
    stage('Pull Source Dev') {
        
        git pull: 'master', changelog: true, poll: false, url: 'git@github.com:aushetty/dbdm.trials.git'
       
        sh """  
                mkdir -p ${WORKSPACE}/${BUILDNUM}
                cd ${WORKSPACE}/${BUILDNUM}       
                find ${WORKSPACE}/ -maxdepth 1 -type f -print0 | xargs -0 mv -t .   
         """
        
    }


    stage ('Build') {
         sh """
            cd ${WORKSPACE}/${BUILDNUM}

            docker build -t sample_pyapp:${BUILDNUM} -t aushetty/sample_pyapp:latest . --no-cache
            docker push aushetty/sample_pyapp:${BUILDNUM}
            docker push aushetty/sample_pyapp:latest

            """

  }

  stage('Deploy'){

         sh """
            /usr/local/bin/kubectl config set-context --current --namepsace=ibm-dev
            /usr/local/bin/kubectl apply -f ${WORKSPACE}/deploysec.yaml
            """

  }
   

}