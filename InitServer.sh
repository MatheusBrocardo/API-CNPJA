#!/bin/bash
export LD_LIBRARY_PATH=/opt/app/oracle/product/19.0.0/dbhome/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export ORACLE_HOME=/opt/app/oracle/product/19.0.0/dbhome/
export TNS_ADMIN=$ORACLE_HOME/network/admin

cd /home/orbi/Documentos/API-CNPJA
source venv/bin/activate

gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 192.168.1.228:3000 
