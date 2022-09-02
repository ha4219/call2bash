rm -rf cgai-lab.github.io
git clone https://github.com/cgai-lab/cgai-lab.github.io.git
cd cgai-lab.github.io
npm i
npm run build
node ./ftp-deploy.js $FTP_ADDRESS $FTP_PORT $FTP_USER $FTP_PASSWORD