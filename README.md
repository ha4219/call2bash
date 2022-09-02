# call2bash

gatsby로 만든 프로젝트를 ftp로 서버에 배포

## the reason it was made

- 사이트 CI/CD를 구현 도중 build한 결과물을 ftp로 특정 서버에 올려야하는데 접근 제한이 있음.

## purpose

- github clone 후 build
- ftp로 서버 upload
- dockerizing
    - node
    - python

## run

1. 먼저 env파일을 만든다.
    ```
    # .env
    FTP_ADDRESS=
    FTP_PORT=
    FTP_USER=
    FTP_PASSWORD=
    ```
2. `app/sh/build2ftp.sh`에서 repo를 수정한다.
    ```
    rm -rf {repo name}
    git clone {git repo}
    cd {repo name}
    npm i
    npm run build
    node ./ftp-deploy.js $FTP_ADDRESS $FTP_PORT $FTP_USER $FTP_PASSWORD
    ```
3. Docker image를 build하고 run
    ```bash
    docker run -it -p {출력 포트}:8000 -e {gatsby build에 필요한 환경변수 추가} -v {.env 파일 위치}:/code/.env -d ha4219/call2bash:latest
    ```